from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('signup/', views.registration_view, name="signup"),
    path('logout/', views.logout_view, name="logout"),
    path('success/', views.success, name="success"),
    path('payment/', views.final_payment, name="payment"),
]
