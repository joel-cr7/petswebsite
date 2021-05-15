from django.shortcuts import render, redirect
from django.views.decorators.csrf import  csrf_exempt
import razorpay
from django.http import HttpResponse
from accounts.views import login_view, registration_view, logout_view
from . models import *
from django.contrib import messages
from django.http import JsonResponse
import json
# Create your views here.


def home(request):
        if request.user.is_authenticated:
                customer=request.user.customer
                order, created=Order.objects.get_or_create(customer=customer, complete=False)
                items=order.orderitem_set.all()
                cartitems = order.get_cart_items
                products= Product.objects.all()  
                all_prods = []
                j=1
                for i in products:
                        if j<=15:
                                all_prods.append(i)
                                j+=1
                        else:
                                break

                dog_products = Product.objects.filter(category__icontains='dog')

                return render(request, 'shop/finalHome.html', {'product':all_prods, 'ci':cartitems, 'dog_products':dog_products})  
        else:
                return redirect('login')


        

def start_page(request):
        if request.user.is_authenticated:
                return redirect('home')
                # customer=request.user.customer
                # order, created=Order.objects.get_or_create(customer=customer, complete=False)
                # items=order.orderitem_set.all()
                # cartitems = order.get_cart_items
                # products= Product.objects.all()   
                # all_prods = []
                # j=1
                # for i in products:
                #         if j<=15:
                #                 all_prods.append(i)
                #                 j+=1
                #         else:
                #                 break
 
                # # n= len(products)
                # return render(request, 'shop/finalHome.html', {'product':all_prods, 'ci':cartitems})
        else:
                products= Product.objects.all() 
                all_prods = []
                j=1
                for i in products:
                        if j<=15:
                                all_prods.append(i)
                                j+=1
                        else:
                                break
                return render(request, 'shop/finalHome.html', {'product':all_prods})

def cart(request):
        if request.user.is_authenticated:
                customer=request.user.customer
                order, created=Order.objects.get_or_create(customer=customer, complete=False)
                items=order.orderitem_set.all()
                cartItems = order.get_cart_items
                pay=order.get_cart_total*100
                context={'items':items, 'order':order,'money':pay, 'cartItems':cartItems}
                return render(request, 'shop/cart.html', context)
        else:
                messages.error(request,'Please Login or Signup to continue shopping !!')
                return redirect('home')
                # items=[]
                # order={'get_cart_total':0, 'get_cart_items':0}
                
        


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

        print('Action: ',action)
        print('ProductId: ',productId)

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


