// Holt den CSRF-Token aus dem HTML-Meta-Tag
const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

// AJAX-Funktion für den Logout-Button
function submitLogoutButton() {
    fetch('/logout/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken
        }
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(data => {
            console.log(data);
            location.reload(); // Zwingend nach dem Logout!
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
}

// Event-Listener für den Button
document.querySelector('#logoutButton').addEventListener('click', function (event) {
    event.preventDefault(); // Verhindert das Standardverhalten des Buttons
    submitLogoutButton(); // Sendet das Formular über AJAX
});
