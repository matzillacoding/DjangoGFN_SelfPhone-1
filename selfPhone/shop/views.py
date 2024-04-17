from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
            # return redirect('login')
        else:
            messages.error(
                request, "Benutzername oder Passwort nicht korrekt.")

    return render(request, 'shop/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "Erfolgreich ausgeloggt.")
    return render(request, 'shop/logout.html')
