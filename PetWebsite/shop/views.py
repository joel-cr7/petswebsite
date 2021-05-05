from django.shortcuts import render, redirect
from django.views.decorators.csrf import  csrf_exempt
import razorpay
from django.http import HttpResponse
from accounts.views import login_view, registration_view, logout_view
from . models import *
# Create your views here.


def home(request):
        products= Product.objects.all()    
        n= len(products)
        return render(request, 'shop/home.html', {'product':products})


def cart(request):
        if request.user.is_authenticated:
                customer=request.user.customer
                order, created=Order.objects.get_or_create(customer=customer, complete=False)
                items=order.orderitem_set.all()
        else:
                items=[]
                order={'get_cart_total':0, 'get_cart_items':0}
        pay=order.get_cart_total*100
        context={'items':items, 'order':order,'money':pay}
        return render(request, 'shop/cart.html', context)


def final_payment(request):
        amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(auth=("rzp_test_K6oU8xWPGy6n1V", "J4oEY2ECYRja6NDw3kmPTfrs"))
        payment = client.order.create({'amount':amount, 'currency':'INR'}) 
        return render(request, 'shop/cart.html', {'payment':payment})


@csrf_exempt
def success(request):
    return HttpResponse("successfully paid !!")
