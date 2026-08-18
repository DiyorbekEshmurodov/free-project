document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('.question-form');
    const periodButtons = document.querySelectorAll('.period-buttons .p-btn');
    const spinner = document.getElementById('loading-spinner');
    const resultBox = document.getElementById('result-section');

    // 1. Form yuborilganda spinner chiqarish
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            if (resultBox) {
                resultBox.style.display = 'none';
            }
            if (spinner) {
                spinner.classList.remove('hidden');
                spinner.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        });
    });

    // 2. Tugmalar bosilganda spinner chiqarish
    periodButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            if (resultBox) {
                resultBox.classList.add('hidden');
            }
            if (spinner) {
                spinner.classList.remove('hidden');
                spinner.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        });
    });

    // 3. AI javobi tayyor bo'lganda natijaga avtomatik scroll qilish
    if (resultBox && !resultBox.classList.contains('hidden')) {
        resultBox.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
});