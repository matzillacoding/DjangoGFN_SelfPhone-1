document.querySelector('#loginForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Verhindert das Standardverhalten des Formulars (Seite neu laden)
    submitLoginForm(); // Sendet das Formular über AJAX
});

function submitLoginForm() {
    const formData = new FormData(document.querySelector('#loginForm'));
    const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    fetch('/login/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': csrftoken, // Setze den CSRF-Token im Header
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
            location.reload(); // Zwingend nach dem Login!
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
        });
}
