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
            location.reload(); //zwingend!
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
}

// Event-Listener für das Absenden des Formulars
document.querySelector('#loginForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Verhindert das Standardverhalten des Formulars (Seite neu laden)
    submitLoginForm(); // Sendet das Formular über AJAX

});