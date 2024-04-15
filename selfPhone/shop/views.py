from django.shortcuts import render

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


def login(request):
    return render(request, 'shop/login.html')
