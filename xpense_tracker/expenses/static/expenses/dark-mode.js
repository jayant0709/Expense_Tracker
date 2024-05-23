const darkMode = document.querySelector('.dark-mode');

document.addEventListener('DOMContentLoaded', function() {
    var mode = localStorage.getItem('mode');
    if (mode === 'dark') {
        document.body.classList.add('dark-mode-variables');
        darkMode.querySelector('span:nth-child(1)').classList.add('active');
        darkMode.querySelector('span:nth-child(2)').classList.add('active');
    }
});
