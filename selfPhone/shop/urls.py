from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),

    path('start/', views.start, name='start'),

    path('product_gallery/', views.product_gallery, name='product_gallery'),

    path('product_details/', views.product_details, name='product_details'),

    path('basket/', views.basket, name='basket'),

    path('checkout/', views.checkout, name='checkout'),

    path('login/', views.login, name='login'),

]
