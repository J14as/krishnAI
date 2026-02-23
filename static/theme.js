// KrishnAI Theme Manager
// Default: dark (cosmic) — override with [data-theme="light"]

const toggleBtn = document.getElementById("theme-toggle");

// Restore saved theme
const savedTheme = localStorage.getItem("krishnai-theme");
if (savedTheme === "light") {
    document.documentElement.setAttribute("data-theme", "light");
    toggleBtn.textContent = "🌙";
} else {
    // dark is default — no attr needed, but show sun icon
    document.documentElement.removeAttribute("data-theme");
    toggleBtn.textContent = "☀️";
}

toggleBtn.addEventListener("click", () => {
    const current = document.documentElement.getAttribute("data-theme");

    if (current === "light") {
        // Switch to dark
        document.documentElement.removeAttribute("data-theme");
        localStorage.setItem("krishnai-theme", "dark");
        toggleBtn.textContent = "☀️";
    } else {
        // Switch to light
        document.documentElement.setAttribute("data-theme", "light");
        localStorage.setItem("krishnai-theme", "light");
        toggleBtn.textContent = "🌙";
    }
});

// Auto-scroll chat window to bottom
window.scrollChatToBottom = function () {
    const w = document.getElementById('chat-window');
    if (w) { w.scrollTop = w.scrollHeight; }
};
setTimeout(() => window.scrollChatToBottom(), 80);
