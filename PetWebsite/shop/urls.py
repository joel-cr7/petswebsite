from django.urls import path
from . import views
from accounts.urls import urlpatterns as account_urls

urlpatterns = [
    path('success/', views.success, name="success"),
    path('payment/', views.final_payment, name="payment"),
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
] + account_urls