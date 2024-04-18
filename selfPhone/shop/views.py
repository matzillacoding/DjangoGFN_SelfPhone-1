from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from asgiref.sync import sync_to_async
from . forms import EigeneUserCreationForm

# Create your views here.


def shop(request):
    return render(request, 'shop/index.html')


def start(request):
    return render(request, 'shop/start.html')


def product_gallery(request):
    return render(request, 'shop/product_gallery.html')


def product_details(request):
    return render(request, 'shop/product_details.html')


def basket(request):
    return render(request, 'shop/basket.html')


def checkout(request):
    return render(request, 'shop/checkout.html')


def test(request):
    return render(request, 'shop/test.html')


def login_user(request):
    seite = 'login'
    messages.success(request, "methode geladen.")
    if request.method == 'POST':
        benutzername = request.POST['benutzername']
        passwort = request.POST['passwort']

        messages.success(request, "POST WAR ERFOLGREICH.")

        benutzer = authenticate(
            request, username=benutzername, password=passwort)

        if benutzer is not None:
            login(request, benutzer)
            # server message
            messages.success(request, "Erfolgreich eingeloggt.")
            return redirect('shop')
        else:
            messages.error(
                request, "Benutzername oder Passwort nicht korrekt.")

    return render(request, 'shop/login.html', {'seite': seite})


def logout_user(request):
    logout(request)
    messages.success(request, "Erfolgreich ausgeloggt.")
    return render(request, 'shop/logout.html')


def register_user(request):
    seite = 'register'
    form = EigeneUserCreationForm
    messages.success(request, "register_user geladen.")

    if request.method == 'POST':
        form = EigeneUserCreationForm(request.POST)
        if form.is_valid():
            benutzer = form.save(commit=False)
            benutzer.save()

            login(request, benutzer)
            messages.success(request, "Benutzerkonto wurde erstellt.")
            return redirect('shop')
        else:
            messages.error(
                request, "Fehler beim Erstellen des Benutzerkontos.")

    return render(request, 'shop/register.html', {'seite': seite, 'form': form})
