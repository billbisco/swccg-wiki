/* Story 429: progressive enhancement for the explicitly marked review sample. */
(function () {
  'use strict';
  function element(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }
  function initialize() {
    document.querySelectorAll('.swccg-vader-viewer-marker').forEach(function (marker, index) {
      var rail = marker.closest('.card-rail');
      if (!rail || rail.dataset.viewerReady) return;
      var portraits = Array.from(rail.querySelectorAll(':scope > .card-portrait'));
      if (portraits.length !== 3 || portraits.some(function (p) { return !p.querySelector('img'); })) return;
      rail.dataset.viewerReady = 'true';
      rail.classList.add('swccg-vader-viewer');
      var labels = ['Historical composite', 'Remastered'];
      var captions = ['Historical Holotable composite · preserved original image', 'CardMaker reconstruction · 2026'];
      var controls = element('div', 'swccg-viewer-choices');
      controls.setAttribute('role', 'group');
      controls.setAttribute('aria-label', 'Full-card image');
      var stage = element('div', 'swccg-viewer-stage');
      var caption = element('p', 'swccg-viewer-caption');
      caption.setAttribute('aria-live', 'polite');
      var buttons = [];
      var panels = portraits.slice(0, 2);
      function select(selected) {
        panels.forEach(function (panel, i) {
          panel.hidden = i !== selected;
          buttons[i].setAttribute('aria-pressed', String(i === selected));
        });
        caption.textContent = captions[selected];
      }
      panels.forEach(function (panel, i) {
        panel.id = 'vader-viewer-' + index + '-' + i;
        panel.classList.add('swccg-viewer-panel');
        var image = panel.querySelector('img');
        image.alt = 'Darth Vader, Virtual Original Set 1 — ' + labels[i];
        var button = element('button', 'swccg-viewer-choice');
        button.type = 'button';
        button.setAttribute('aria-controls', panel.id);
        button.setAttribute('aria-label', labels[i]);
        var preview = image.cloneNode(false);
        preview.removeAttribute('width');
        preview.removeAttribute('height');
        preview.alt = '';
        preview.setAttribute('aria-hidden', 'true');
        button.append(preview, element('span', '', labels[i]));
        button.addEventListener('click', function () { select(i); });
        button.addEventListener('keydown', function (event) {
          if (event.key !== 'ArrowLeft' && event.key !== 'ArrowRight' && event.key !== 'Home' && event.key !== 'End') return;
          event.preventDefault();
          var next = event.key === 'Home' ? 0 : event.key === 'End' ? 1 : 1 - i;
          buttons[next].focus();
          select(next);
        });
        buttons.push(button);
        controls.append(button);
        stage.append(panel);
      });
      var viewer = element('div', 'swccg-viewer-main');
      viewer.append(controls, stage, caption);
      rail.insertBefore(viewer, rail.firstChild);
      var slip = portraits[2];
      slip.classList.add('swccg-viewer-slip');
      slip.querySelector('img').alt = 'Publisher slip for Darth Vader, Original Set 1, later wording';
      slip.append(element('p', 'swccg-viewer-caption', 'Publisher slip · matching text version'));
      var compare = element('button', 'swccg-viewer-compare', 'Compare images');
      compare.type = 'button';
      compare.setAttribute('aria-haspopup', 'dialog');
      slip.after(compare);
      var dialog = element('dialog', 'swccg-viewer-dialog');
      var heading = element('h2', '', 'Darth Vader — image comparison');
      heading.id = 'vader-comparison-title-' + index;
      dialog.setAttribute('aria-labelledby', heading.id);
      var close = element('button', 'swccg-viewer-close', 'Close comparison');
      close.type = 'button';
      close.autofocus = true;
      var comparison = element('div', 'swccg-viewer-comparison');
      portraits.forEach(function (portrait, i) {
        var figure = element('figure', i === 2 ? 'swccg-comparison-slip' : '');
        var link = portrait.querySelector('a').cloneNode(true);
        var fullImage = link.querySelector('img');
        fullImage.src = fullImage.src.replace(/\/thumb\/(.*)\/[^/]+$/, '/$1');
        fullImage.removeAttribute('srcset');
        fullImage.removeAttribute('height');
        fullImage.width = 350;
        link.querySelectorAll('[hidden]').forEach(function (node) { node.removeAttribute('hidden'); });
        figure.append(link, element('figcaption', '', i < 2 ? captions[i] : 'Publisher slip · matching text version'));
        comparison.append(figure);
      });
      dialog.append(close, heading, comparison);
      document.body.append(dialog);
      compare.addEventListener('click', function () {
        if (typeof dialog.showModal === 'function') dialog.showModal();
        else { dialog.setAttribute('open', ''); close.focus(); }
      });
      function closeDialog() {
        if (typeof dialog.close === 'function') dialog.close();
        else { dialog.removeAttribute('open'); compare.focus(); }
      }
      close.addEventListener('click', closeDialog);
      dialog.addEventListener('close', function () { compare.focus(); });
      dialog.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') { event.preventDefault(); closeDialog(); }
      });
      marker.hidden = true;
      select(0);
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initialize);
  else initialize();
  if (window.mw && mw.hook) mw.hook('wikipage.content').add(initialize);
}());
