// static/js/main.js

document.addEventListener("DOMContentLoaded", function() {
    console.log("Gym Daily - High-Tech Bio-Metric tizimi muvaffaqiyatli ishga tushdi!");

    // "A'ZO BO'LISH" tugmasiga bosilganda ravon (smooth) tushish
    const mainBtn = document.querySelector('.btn-danger-custom');
    if (mainBtn) {
        mainBtn.addEventListener('click', function(e) {
            e.preventDefault();
            alert("A'zolik bo'limiga yo'naltirildingiz!");
        });
    }

    // Kartochkalarga sichqoncha kelganda interaktivlik berish
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.cursor = 'pointer';
        });
    });
});