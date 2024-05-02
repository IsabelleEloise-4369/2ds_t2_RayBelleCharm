document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const menuItems = document.querySelector('.header-container__menu__itens');

    menuToggle.addEventListener('click', function() {
        menuItems.classList.toggle('show');
    });
});