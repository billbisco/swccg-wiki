/* Stories 384/429: progressive enhancement for the two bounded review samples. */
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
      var cardName = marker.dataset.cardName || 'Card';
      var labels = ['Original', 'Remastered'];
      var controls = element('div', 'swccg-viewer-choices');
      controls.setAttribute('role', 'group');
      controls.setAttribute('aria-label', 'Full-card image');
      var stage = element('div', 'swccg-viewer-stage');
      var buttons = [];
      var panels = portraits.slice(0, 2);
      function select(selected) {
        panels.forEach(function (panel, i) {
          panel.hidden = i !== selected;
          buttons[i].setAttribute('aria-pressed', String(i === selected));
        });
      }
      panels.forEach(function (panel, i) {
        panel.id = 'vader-viewer-' + index + '-' + i;
        panel.classList.add('swccg-viewer-panel');
        var image = panel.querySelector('img');
        image.alt = cardName + ', Virtual Original Set 1 — ' + labels[i];
        var button = element('button', 'swccg-viewer-choice', labels[i]);
        button.type = 'button';
        button.setAttribute('aria-controls', panel.id);
        button.setAttribute('aria-label', labels[i]);
        button.title = i === 0 ? 'Historical Holotable composite' : 'CardMaker reconstruction';
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
      viewer.append(stage);
      rail.insertBefore(viewer, rail.firstChild);
      var slip = portraits[2];
      slip.classList.add('swccg-viewer-slip');
      slip.querySelector('img').alt = 'Publisher slip for ' + cardName + ', Original Set 1, later wording';
      slip.after(controls);
      marker.hidden = true;
      select(0);
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initialize);
  else initialize();
  if (window.mw && mw.hook) mw.hook('wikipage.content').add(initialize);
}());
