
// Open menu on burger icon

const menu = document.getElementById("icon-menu");
const menuSlider = document.getElementById("navigation");

menu.addEventListener('click', function() {
    menuSlider.classList.toggle("visible");
})