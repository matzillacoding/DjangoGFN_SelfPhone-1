$(document).ready(function () {
    // Funktion, um das Login-Formular zu laden
    function loadLoginForm() {
        $.ajax({
            url: '/login/', // URL für das Login-View
            type: 'get',
            success: function (response) {
                $('.login-slider').html(response);
            }
        });
    }

    // Funktion, um das Registrierungsformular zu laden
    function loadRegisterForm() {
        $.ajax({
            url: '/register/', // URL für das Register-View
            type: 'get',
            success: function (response) {
                $('.login-slider').html(response);
            }
        });
    }

    // Event-Handler für den Wechsel zum Registrierungsformular
    $(document).on('click', 'a[href="{% url \'register\' %}"]', function (event) {
        event.preventDefault();
        loadRegisterForm();
    });

    // Initial das Login-Formular laden, wenn die Seite geladen wird
    loadLoginForm();
});
