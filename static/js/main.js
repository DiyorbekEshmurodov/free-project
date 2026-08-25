document.addEventListener("DOMContentLoaded", function() {

    // 1. Typewriter (Faqat ushbu elementlar bor sahifada ishlaydi)
    const el1 = document.getElementById("line1");
    const el2 = document.getElementById("line2");

    if (el1 && el2) {
        const text1 = "Fitness & AI Planner and Life GYM";
        const text2 = "for everyone";
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
    }
});

// 2. Userbar Dropdown menyuni ochish va yopish
function toggleUserMenu() {
    const dropdown = document.getElementById('userDropdown');
    if (dropdown) {
        dropdown.classList.toggle('show');
    }
}

// 3. Ekran boshqa joyiga bosilganda menyuni yopish
window.addEventListener('click', function(e) {
    const btn = document.getElementById('userMenuBtn');
    const dropdown = document.getElementById('userDropdown');
    if (btn && dropdown && !btn.contains(e.target) && !dropdown.contains(e.target)) {
        dropdown.classList.remove('show');
    }
});