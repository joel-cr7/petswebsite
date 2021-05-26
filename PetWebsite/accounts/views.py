from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from accounts.forms import RegistrationForm, cust_form
from django.http import HttpResponse
from shop.models import *

# Create your views here.
def login_view(request):
    context= {}
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:   
            login(request, user)
            return redirect('home')
        else:      
            context['login_form']="Invalid username or password !!"

    return render(request,'accounts/login.html', context)    


def registration_view(request):
    context = {}
    if request.POST:                      
        form = RegistrationForm(request.POST)
        customer_form = cust_form(request.POST)
        if form.is_valid() and customer_form.is_valid():                      
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
            return redirect('home')
            # return render(request, 'shop/home.html')
        else:
            context['registration_form'] = form    
    else:                                        
        form = RegistrationForm()
        customer_form=cust_form()
        context['registration_form'] = form
        context['customer_form'] = customer_form
    return render(request,'accounts/signup.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')