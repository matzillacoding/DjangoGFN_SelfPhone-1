// AJAX-Funktion für den logout knopf
function submitLogoutForm() {
    const formData = new FormData(document.querySelector('#logoutForm'));

    fetch('/logout/', {
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
            location.reload();
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
}

// Event-Listener für das Absenden des Formulars
document.querySelector('#logoutForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Verhindert das Standardverhalten des Formulars (Seite neu laden)
    submitLogoutForm(); // Sendet das Formular über AJAX

});