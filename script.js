// Simple touch animation example (you can expand on this)
const socialMediaLinks = document.querySelectorAll('#social-media a');

socialMediaLinks.forEach(link => {
    link.addEventListener('touchstart', () => {
        link.style.backgroundColor = '#ccc'; // Change background on touch
    });

    link.addEventListener('touchend', () => {
        link.style.backgroundColor = '#f0f0f0'; // Reset background after touch
    });
});
