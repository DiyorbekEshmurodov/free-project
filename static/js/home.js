document.addEventListener("DOMContentLoaded", function () {
    // AOS Animatsiyasini ishga tushirish
    if (typeof AOS !== 'undefined') {
        AOS.init({
            once: true,
            duration: 800,
            offset: 100
        });
    }
});
function previewImage(event) {
    const input = event.target;
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const preview = document.getElementById('avatar-preview');
            const placeholder = document.getElementById('avatar-placeholder');

            preview.src = e.target.result;
            preview.style.display = 'block';
            if (placeholder) {
                placeholder.style.display = 'none';
            }
        }
        reader.readAsDataURL(input.files[0]);
    }
}