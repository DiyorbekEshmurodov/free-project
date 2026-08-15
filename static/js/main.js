document.addEventListener("DOMContentLoaded", function() {

    // 1. Theme Toggle (Kun va Tun rejimini almashtirish)
    const toggleBtn = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;

    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            let currentTheme = htmlElement.getAttribute('data-theme');
            let newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            htmlElement.setAttribute('data-theme', newTheme);

            // Mana bu joyda 'M' o'rniga oy emojisi ('🌙') qo'yildi:
            toggleBtn.textContent = newTheme === 'dark' ? '☀️' : '🌜';
        });
    }

    // 2. Typewriter (Harf-ma-harf yozilish effekti)
    const text1 = "Fitness & AI Planner and Life GYM";
    const text2 = "for everyone";

    const el1 = document.getElementById("line1");
    const el2 = document.getElementById("line2");

    if (!el1 || !el2) return;

    let i = 0;
    function typeWriter1() {
        if (i < text1.length) {
            el1.textContent += text1.charAt(i);
            el1.style.borderColor = "var(--primary-blue)";
            i++;
            setTimeout(typeWriter1, 70);
        } else {
            el1.style.borderColor = "transparent";
            let j = 0;
            function typeWriter2() {
                if (j < text2.length) {
                    el2.textContent += text2.charAt(j);
                    el2.style.borderColor = "var(--primary-blue)";
                    j++;
                    setTimeout(typeWriter2, 70);
                } else {
                    el2.style.borderColor = "transparent";
                }
            }
            setTimeout(typeWriter2, 300);
        }
    }
    typeWriter1();
});
// Userbar Dropdown menyuni ochish va yopish
function toggleUserMenu() {
    const dropdown = document.getElementById('userDropdown');
    if (dropdown) {
        dropdown.classList.toggle('show');
    }
}

// Ekran boshqa joyiga bosilganda menyuni yopish
window.addEventListener('click', function(e) {
    const btn = document.getElementById('userMenuBtn');
    const dropdown = document.getElementById('userDropdown');
    if (btn && dropdown && !btn.contains(e.target) && !dropdown.contains(e.target)) {
        dropdown.classList.remove('show');
    }
});