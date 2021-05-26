from django.urls import path
from . import views
from accounts.urls import urlpatterns as account_urls

urlpatterns = [
    path('success/', views.success, name="success"),
    path('payment/', views.final_payment, name="payment"),
    path('', views.start_page, name="start_page"),
    path('home/', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('update_item/', views.updateItem, name="update_item"),
    path('search/', views.search, name="search"),
] + account_urls
