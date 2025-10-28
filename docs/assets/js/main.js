// Inject navbar and footer into pages and init animations
(async function initSite() {
  const prefixes = ['', '../', '../../', '../../../', '../../../../'];
  async function fetchWithFallback(relativePath) {
    for (const p of prefixes) {
      try {
        const res = await fetch(p + relativePath);
        if (res.ok) return { text: await res.text(), prefix: p };
      } catch (_) { /* ignore */ }
    }
    throw new Error('Unable to load ' + relativePath);
  }

  const navbar = document.getElementById('navbar-root');
  const footer = document.getElementById('footer-root');

  try {
    let detectedPrefix = '';
    if (navbar) {
      const { text, prefix } = await fetchWithFallback('partials/navbar.html');
      detectedPrefix = prefix;
      navbar.innerHTML = text;
      rewriteDocLinks(navbar, detectedPrefix);
    }
    if (footer) {
      // If we didn't detect prefix above (no navbar), detect via footer
      const result = await fetchWithFallback('partials/footer.html');
      const prefix = result.prefix || detectedPrefix;
      footer.innerHTML = result.text;
      const yearEl = document.getElementById('year');
      if (yearEl) yearEl.textContent = new Date().getFullYear();
      rewriteDocLinks(footer, prefix);
    }
  } catch (e) {
    console.error('Failed to inject partials', e);
  }

  if (window.AOS) {
    AOS.init({ once: true, duration: 700, offset: 80, easing: 'ease-out' });
  }
})();

function rewriteDocLinks(root, prefix) {
  root.querySelectorAll('a[href^="/docs/"]').forEach(a => {
    const rest = a.getAttribute('href').slice('/docs/'.length);
    a.setAttribute('href', prefix + rest);
  });
  root.querySelectorAll('img[src^="/docs/"]').forEach(img => {
    const rest = img.getAttribute('src').slice('/docs/'.length);
    img.setAttribute('src', prefix + rest);
  });
}

// Helper to set active nav link based on pathname
(function setActiveNav() {
  const path = location.pathname.replace(/\/$/, '');
  function markActive(selector) {
    const links = document.querySelectorAll(selector);
    links.forEach(link => {
      const href = link.getAttribute('href');
      if (!href) return;
      const normalized = href.replace(/\/$/, '');
      if (normalized && path.endsWith(normalized)) {
        link.classList.add('active');
      }
    });
  }
  markActive('a.nav-link');
})();
