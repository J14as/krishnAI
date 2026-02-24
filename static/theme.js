(function () {
    const btn = document.getElementById('theme-toggle');
    const STORAGE_KEY = 'krishnai-theme';

    // Apply saved theme on load
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
        if (btn) btn.textContent = '🌙';
    } else {
        if (btn) btn.textContent = '☀️';
    }

    if (btn) {
        btn.addEventListener('click', function () {
            const isLight = document.documentElement.getAttribute('data-theme') === 'light';
            if (isLight) {
                document.documentElement.removeAttribute('data-theme');
                localStorage.setItem(STORAGE_KEY, 'dark');
                btn.textContent = '☀️';
            } else {
                document.documentElement.setAttribute('data-theme', 'light');
                localStorage.setItem(STORAGE_KEY, 'light');
                btn.textContent = '🌙';
            }
        });
    }
})();
