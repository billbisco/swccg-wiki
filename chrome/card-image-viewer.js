/* work#443: exact-state image renditions. Activation is limited by the pilot manifest. */
(function (root, factory) {
  'use strict';
  var api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  // mw.config exists during startup before mediawiki.base installs loader.using.
  // Plain RLQ callbacks also run early; dependency entries wait for the base module.
  else (root.RLQ = root.RLQ || []).push([['mediawiki.base'], function () { api.start(root); }]);
}(typeof window === 'undefined' ? globalThis : window, function () {
  'use strict';
  var OPTION = 'swccg-card-images';
  function preference(value) { return value === 'remastered' ? value : 'original'; }
  function eligible(card) {
    return (card.renditions || []).filter(function (r) {
      return ['original', 'remastered'].includes(r.kind) && r.state === card.state &&
        r.language === card.language && r.file;
    });
  }
  function choose(card, preferred, available) {
    var options = eligible(card).filter(function (r) { return available(r); });
    var selected = options.find(function (r) { return r.kind === preference(preferred); }) || options[0];
    var original = options.find(function (r) { return r.kind === 'original'; });
    var remaster = options.find(function (r) { return r.kind === 'remastered'; });
    return { selected: selected, pair: !!(original && remaster && original.file !== remaster.file &&
      !(original.sha256 && original.sha256 === remaster.sha256)) };
  }
  function start(win) {
    if (win.swccgCardImages) { win.swccgCardImages.initialize(); return; }
    var doc = win.document;
    var config = win.mw && win.mw.config.get('swccgCardImagePilot');
    if (!config) return;
    // Vector legacy uses a fixed 1120px viewport. Fit only these allowlisted
    // review pages to phones; keep the site's skin/configuration untouched.
    var viewport = doc.querySelector('meta[name="viewport"]');
    if (viewport && win.screen.width > 0 && win.screen.width <= 720) {
      viewport.content = 'width=device-width, initial-scale=1';
    }
    var words = config.messages;
    var controllers = [];
    var saved = 'original';
    var preferenceReady;
    var loggedIn = !!win.mw.config.get('wgUserName');
    var api;
    function node(tag, className, text) {
      var el = doc.createElement(tag);
      if (className) el.className = className;
      if (text) el.textContent = text;
      return el;
    }
    function fileName(portrait) {
      var link = portrait.querySelector('a[href]');
      if (!link) return '';
      try {
        return decodeURIComponent(link.getAttribute('href')).split('File:')[1].replace(/_/g, ' ');
      } catch (error) { return ''; }
    }
    function readPreference() {
      if (!loggedIn) {
        try { saved = preference(win.localStorage.getItem(OPTION)); } catch (error) { saved = 'original'; }
        return Promise.resolve(saved);
      }
      // Never put an account value into public HTML/config or guest localStorage.
      return Promise.resolve().then(function () { return win.mw.loader.using('mediawiki.api'); }).then(function () {
        api = new win.mw.Api();
        return api.get({ action: 'query', meta: 'userinfo', uiprop: 'options', assert: 'user' });
      }).then(function (response) {
        saved = preference(response.query.userinfo.options[OPTION]);
        return saved;
      }).catch(function () { saved = 'original'; return saved; });
    }
    function savePreference(value) {
      value = preference(value);
      if (loggedIn) {
        if (!api) return Promise.reject(new Error('Account preference service unavailable'));
        return Promise.resolve().then(function () {
          return api.postWithToken('csrf', { action: 'options', change: OPTION + '=' + value, assert: 'user' });
        })
          .then(function () { saved = value; });
      }
      try { win.localStorage.setItem(OPTION, value); saved = value; return Promise.resolve(); }
      catch (error) { return Promise.reject(error); }
    }
    function settings() {
      if (!config.settingsPage) return;
      if (doc.querySelector('.swccg-card-image-settings')) return;
      var content = doc.querySelector('.swccg-card-image-preferences-target');
      if (!content) return;
      var box = node('form', 'swccg-card-image-settings');
      var label = node('label', '', words.setting);
      var select = node('select');
      select.id = 'swccg-card-image-default'; label.htmlFor = select.id;
      ['original', 'remastered'].forEach(function (kind) {
        var option = node('option', '', words[kind]); option.value = kind; select.append(option);
      });
      select.value = saved;
      var save = node('button', '', words.save); save.type = 'submit';
      var status = node('span', 'swccg-card-image-status'); status.setAttribute('role', 'status');
      box.append(label, select, save, status);
      box.addEventListener('submit', function (event) {
        event.preventDefault(); save.disabled = true;
        savePreference(select.value).then(function () { status.textContent = words.saved; })
          .catch(function () { select.value = saved; status.textContent = words.failed; })
          .finally(function () { save.disabled = false; });
      });
      content.append(box);
    }
    function attach(marker) {
      var card = config.cards[marker.dataset.cardImageKey];
      var rail = marker.closest('.card-rail');
      if (!rail) return;
      var key = JSON.stringify(card || null);
      if (rail.swccgImageController) {
        if (rail.swccgImageController.key === key) return;
        rail.swccgImageController.destroy();
      }
      if (!card) return;
      var portraits = Array.from(rail.querySelectorAll(':scope > .card-portrait'));
      var byFile = {};
      portraits.forEach(function (p) { byFile[fileName(p)] = p; });
      var panels = eligible(card).map(function (r) {
        return { rendition: r, panel: byFile[r.file.replace(/_/g, ' ')] };
      }).filter(function (p) { return p.panel && p.panel.querySelector('img'); });
      if (!panels.length) return; // Preserve native missing-image output.
      rail.dataset.cardImagesReady = 'true'; rail.classList.add('swccg-card-images');
      var stage = node('div', 'swccg-card-image-stage');
      var controls = node('div', 'swccg-card-image-choices');
      controls.setAttribute('role', 'group'); controls.setAttribute('aria-label', words.group);
      var selection = saved;
      var broken = new Set();
      var buttons = {};
      var listeners = [];
      panels.forEach(function (p, i) {
        var image = p.panel.querySelector('img');
        p.panel.id = 'swccg-card-image-' + controllers.length + '-' + i;
        image.alt = card.label + ' — ' + words[p.rendition.kind];
        var button = node('button', '', words[p.rendition.kind]); button.type = 'button';
        button.setAttribute('aria-controls', p.panel.id);
        button.addEventListener('click', function () { selection = p.rendition.kind; render(); });
        button.addEventListener('keydown', function (event) {
          if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
          event.preventDefault();
          var target = event.key === 'Home' ? 'original' : event.key === 'End' ? 'remastered' :
            p.rendition.kind === 'original' ? 'remastered' : 'original';
          if (buttons[target]) { buttons[target].focus(); buttons[target].click(); }
        });
        buttons[p.rendition.kind] = button; controls.append(button); stage.append(p.panel);
        var onError = function () { broken.add(p.rendition.file); render(); };
        var onLoad = function () { broken.delete(p.rendition.file); render(); };
        image.addEventListener('error', onError);
        image.addEventListener('load', onLoad);
        listeners.push(function () {
          image.removeEventListener('error', onError); image.removeEventListener('load', onLoad);
        });
        if (image.complete && !image.naturalWidth) broken.add(p.rendition.file);
      });
      var slip = card.slip && byFile[card.slip.replace(/_/g, ' ')];
      portraits.forEach(function (p) {
        if (p !== slip && !panels.some(function (entry) { return entry.panel === p; })) p.hidden = true;
      });
      // Put controls after the full-card stage AND its publisher slip, before Info.
      rail.insertBefore(stage, rail.firstChild);
      if (slip) stage.after(slip);
      (slip || stage).after(controls);
      marker.hidden = true;
      rail.swccgImageController = { key: key, destroy: function () {
        listeners.forEach(function (remove) { remove(); });
        portraits.forEach(function (p) { p.hidden = false; stage.before(p); });
        stage.remove(); controls.remove(); marker.hidden = false;
        rail.classList.remove('swccg-card-images'); delete rail.dataset.cardImagesReady;
        delete rail.swccgImageController;
      } };
      function render() {
        var result = choose(card, selection, function (r) {
          return !broken.has(r.file) && panels.some(function (p) { return p.rendition.file === r.file; });
        });
        controls.hidden = !result.pair;
        panels.forEach(function (p) {
          var active = result.selected && p.rendition.file === result.selected.file;
          // If all fail, keep a native image/File link rather than an empty stage.
          p.panel.hidden = result.selected ? !active : p !== panels[0];
          buttons[p.rendition.kind].setAttribute('aria-pressed', String(!!active));
        });
      }
      controllers.push({ render: render }); render();
    }
    function initialize() {
      if (!preferenceReady) preferenceReady = readPreference();
      return preferenceReady.then(function () {
        settings();
        doc.querySelectorAll('.swccg-card-image-marker').forEach(attach);
      });
    }
    win.swccgCardImages = { initialize: initialize };
    if (doc.readyState === 'loading') doc.addEventListener('DOMContentLoaded', initialize);
    else initialize();
    if (win.mw.hook) win.mw.hook('wikipage.content').add(initialize);
  }
  return { preference: preference, eligible: eligible, choose: choose, start: start };
}));
