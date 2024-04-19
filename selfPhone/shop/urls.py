from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),

    path('product_gallery/', views.product_gallery, name='product_gallery'),

    path('product_details/', views.product_details, name='product_details'),

    path('basket/', views.basket, name='basket'),

    path('checkout/', views.checkout, name='checkout'),

    path('login/', views.login_user, name='login'),

    path('logout/', views.logout_user, name='logout'),

    path('test/', views.test, name='test'),

    path('register/', views.register_user, name='register'),

    # path('shop_backend/', views.shopBackend, name='shop_backend')

]
