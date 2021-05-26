from django.shortcuts import render, redirect
from django.views.decorators.csrf import  csrf_exempt
import razorpay
from django.http import HttpResponse
from accounts.views import login_view, registration_view, logout_view
from . models import *
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
import json

# Create your views here.
def home(request):
        products= Product.objects.all()  
        item1 = Product.objects.filter(product_name__icontains='double bowl')
        item2 = Product.objects.filter(product_name__icontains='cat tunnel')
        item3 = Product.objects.filter(product_name__icontains='clear glass')
        item4 = Product.objects.filter(product_name__icontains='tees for dog')
        item5 = Product.objects.filter(product_name__icontains='automatic')
        new_arrivals = [item1,item2,item3,item4,item5]
        all_prods = []
        j=1
        for i in products:
                if j<=15:
                        all_prods.append(i)
                        j+=1
                else:
                        break
        dog_products = Product.objects.filter(category__icontains='dog')
        cat_products = Product.objects.filter(category__icontains='cat')
        fish_products = Product.objects.filter(category__icontains='fish')
        bird_products = Product.objects.filter(category__icontains='bird')

        if request.user.is_authenticated:
                customer=request.user.customer
                order, created=Order.objects.get_or_create(customer=customer, complete=False)
                items=order.orderitem_set.all()
                cartitems = order.get_cart_items
                return render(request, 'shop/finalHome.html', {'product':all_prods, 'ci':cartitems, 'dog_products':dog_products, 
                'cat_products':cat_products, 'fish_products':fish_products, 'bird_products':bird_products,'new_arrivals':new_arrivals})  
        else:
                return render(request, 'shop/finalHome.html', {'product':all_prods, 'dog_products':dog_products, 
                'cat_products':cat_products, 'fish_products':fish_products, 'bird_products':bird_products, 'new_arrivals':new_arrivals})  


def start_page(request):
        if request.user.is_authenticated:
                return redirect('home')
        else:
                products= Product.objects.all() 
                item1 = Product.objects.filter(product_name__icontains='double bowl')
                item2 = Product.objects.filter(product_name__icontains='cat tunnel')
                item3 = Product.objects.filter(product_name__icontains='clear glass')
                item4 = Product.objects.filter(product_name__icontains='tees for dog')
                item5 = Product.objects.filter(product_name__icontains='automatic')
                new_arrivals = [item1,item2,item3,item4,item5]
                all_prods = []
                j=1
                for i in products:
                        if j<=15:
                                all_prods.append(i)
                                j+=1
                        else:
                                break
                return render(request, 'shop/finalHome.html', {'product':all_prods, 'new_arrivals':new_arrivals})

def cart(request):
        if request.user.is_authenticated:
                customer=request.user.customer
                order, created=Order.objects.get_or_create(customer=customer, complete=False)
                items=order.orderitem_set.all()
                cartItems = order.get_cart_items
                pay=order.get_cart_total*100
                context={'items':items, 'order':order,'money':pay, 'ci':cartItems}
                return render(request, 'shop/cart.html', context)
        else:
                return redirect('home')
                
        
def final_payment(request):
        amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(auth=("rzp_test_K6oU8xWPGy6n1V", "J4oEY2ECYRja6NDw3kmPTfrs"))
        payment = client.order.create({'amount':amount, 'currency':'INR'}) 
        return render(request, 'shop/cart.html', {'payment':payment})


@csrf_exempt
def success(request):
    return HttpResponse("successfully paid !!")


def updateItem(request):
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']

        customer = request.user.customer
        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
                orderItem.quantity = (orderItem.quantity + 1)

        elif action == 'remove':
                orderItem.quantity = (orderItem.quantity - 1)

        orderItem.save()

        if orderItem.quantity <= 0:
                orderItem.delete()
        return JsonResponse('item was added', safe=False) 


def search(request):
        kw = request.GET.get("keyword")
        result = Product.objects.filter(Q(category__icontains=kw) | Q(desc__icontains=kw) | Q(product_name__icontains=kw))
        if request.user.is_authenticated:
                customer=request.user.customer
                order, created=Order.objects.get_or_create(customer=customer, complete=False)
                items=order.orderitem_set.all()
                cartitems = order.get_cart_items
                return render(request, 'shop/search.html',{'result':result, 'ci':cartitems})
        else:
                return render(request, 'shop/search.html',{'result':result})