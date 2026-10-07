(function () {
  function inject(sel, url, where) {
    if (document.querySelector(sel)) return;
    fetch(url, { credentials: "same-origin" })
      .then(function (r) { return r.text(); })
      .then(function (html) {
        var wrap = document.createElement("div");
        wrap.innerHTML = html.trim();
        var node = wrap.firstElementChild;
        if (!node) return;
        if (where === "start") document.body.insertBefore(node, document.body.firstChild);
        else document.body.appendChild(node);
      })
      .catch(function () {});
  }
  if (!document.body || !document.body.classList.contains("mediawiki")) {
    return;
  }
  /* Wiki uses Vector sidebar + tabs like LOTR; landing keeps the dark chrome. */
})();
