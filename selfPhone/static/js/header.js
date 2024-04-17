
// Header Nav Events & Sliders

// Slider
const sliderMenu = document.querySelector("#navigation");
const sliderBasket = document.querySelector(".basket-slider");
const sliderAccount = document.querySelector(".login-slider");

// Icons
const iconMenu = document.querySelector("#icon-menu");
const iconBasket = document.querySelector("#icon-basket");
const iconAccount = document.querySelector("#icon-account");
const iconsClose = Array.from(document.querySelectorAll(".icon-close"));
const allIcons = [iconMenu, iconBasket, iconAccount];

// Various
const overlay = document.querySelector(".overlay");
const allElements = [sliderMenu, sliderBasket, sliderAccount, iconMenu, iconBasket, iconAccount, overlay];


// Functions
function hideAll() {
    allElements.forEach(element => {
        element.classList.remove("visible");
    })
}

function showOverlay() {
    overlay.classList.add("visible");
}

function open(icon, slider) {
    hideAll();
    showOverlay();
    [icon, slider].forEach(element => {
        element.classList.add("visible");
    });

    // Fokus auf das Benutzername-Feld setzen, wenn die Slidebar geöffnet wird
    /*if (slider === sliderAccount) {
        document.querySelector("#InputEmail").focus();
    }*/
}


// Events

allIcons.forEach(icon => {
    icon.addEventListener('click', function () {
        overlay.classList.add("visible");
    })
})

iconMenu.addEventListener('click', function () {
    open(iconMenu, sliderMenu);
})

iconBasket.addEventListener('click', function () {
    open(iconBasket, sliderBasket);
})

iconAccount.addEventListener('click', function () {
    open(iconAccount, sliderAccount);
})

overlay.addEventListener('click', function () {
    hideAll();
})

iconsClose.forEach(icon => {
    icon.addEventListener('click', function () {
        hideAll();
    })
})

// AJAX-Funktion für das Formular im Slider
function submitLoginForm() {
    const formData = new FormData(document.querySelector('#loginForm'));

    fetch('/login/', {
        method: 'POST',
        body: formData,
        'X-CSRFToken': csrftoken,
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            // Hier kannst du die Antwort des Servers verarbeiten, z.B. Erfolg oder Fehlermeldung anzeigen
            console.log(data);
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
}

// Event-Listener für das Absenden des Formulars
document.querySelector('#loginForm').addEventListener('submit', function (event) {
    //event.preventDefault(); // Verhindert das Standardverhalten des Formulars (Seite neu laden)
    submitLoginForm(); // Sendet das Formular über AJAX
});