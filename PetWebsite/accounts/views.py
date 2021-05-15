from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from accounts.forms import RegistrationForm, cust_form
from django.http import HttpResponse
from shop.models import *


# from django.http import HttpResponse
# from django.contrib import auth
# from django.contrib.auth.models import User
# from .models import customUser

# Create your views here.
def login_view(request):
    context= {}
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:    # if username and password is correct
            login(request, user)

            # customer=request.user.customer
            # order, created=Order.objects.get_or_create(customer=customer, complete=False)
            # items=order.orderitem_set.all()
            # cartItems = order.get_cart_items
            # products= Product.objects.all()

            # return render(request, 'shop/homeM.html', {'product':products, 'cartItems':cartItems})
            return redirect('home')

            # return render(request, 'shop/homeM.html')
        else:       # if username or password incorrect
            context['login_form']="Invalid username or password !!"



    return render(request,'accounts/login.html', context)
    # user=request.user
    # if user.is_authenticated:
    #     return HttpResponse("User logged in successfully")

    # if request.POST:
    #     form=LoginAuthenticationForm(request.POST)
    #     if form.is_valid():
    #         username=request.POST['username']
    #         password=request.POST['password']
    #         user=authenticate(username=username, password=password)
                            
    #         if user:
    #             login(request, user)
    #             return HttpResponse("User logged in successfully")

    # else:
    #     form=LoginAuthenticationForm()

    # context['login_form']=form
    # return render(request,'accounts/login.html', context)
    # return render(request,'accounts/login.html')
    # if request.method=="POST":
    #     user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        
    #     if user is not None:
    #         auth.login(request,user)
    #         return HttpResponse("Login successful !!")
    #     else:
    #         return HttpResponse("login failed !!")
    # else:
    


def registration_view(request):
    context = {}
    if request.POST:                             # for post request
        form = RegistrationForm(request.POST)
        customer_form = cust_form(request.POST)
        if form.is_valid() and customer_form.is_valid():                      # if user entered proper format of info
            register_form=form.save()
            c_form=customer_form.save(False)
            c_form.user=register_form
            c_form.name=register_form.first_name
            c_form.email=register_form.email
            c_form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            phone_no = form.cleaned_data.get('phone_no')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return render(request, 'shop/home.html')
        else:
            context['registration_form'] = form     # if form not valid, then too send that errenous form to the template
    else:                                        # for get request
        form = RegistrationForm()
        customer_form=cust_form()
        context['registration_form'] = form
        context['customer_form'] = customer_form
    return render(request,'accounts/signup.html', context)
#     if request.method == "POST":
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user=User.objects.get(username=request.POST['username'])
#                 return HttpResponse("Username exists !!")
#             except User.DoesNotExist:
#                 user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
#                 phone_no=request.POST['phone']
#                 email=request.POST['email']
#                 new_user=customUser(phone_no=phone_no, email=email, user=user)
#                 # new_user.save()
#                 auth.login(request,user)
#                 return HttpResponse("User created Successfully !!")
#         else:
#             return HttpResponse("Signed in failed")
#     else:
#         return render(request,'accounts/signup.html')

#To logout the user
def logout_view(request):
    logout(request)
    return redirect('start_page')



