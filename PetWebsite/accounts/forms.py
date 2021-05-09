from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account
from shop.models import Customer
from django.contrib.auth import authenticate
from django.forms import ModelForm


# As we created custom user models so we need to create custom registration forms
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30 ,error_messages={'required':'First name Required*'})   # this will show error if no input is provided
    last_name = forms.CharField(max_length=30, error_messages={'required':'Last name Required*'})   # this will show error if no input is provided
    email = forms.EmailField(max_length=60, error_messages={'required':'Email address Required*'})  # this will show error if no input is provided
    phone_no = forms.CharField(max_length=10, error_messages={'required':'Phone no. Required*'})  # this will show error if no input is provided
    username = forms.CharField(max_length=30, error_messages={'required':'Username Required*'})  # this will show error if no input is provided
    password1 = forms.CharField(widget=forms.PasswordInput,error_messages={'required':'Password Required*'})   # this will show error if no input is provided
    password2 = forms.CharField(widget=forms.PasswordInput,error_messages={'required':'Retype Password'})   # this will show error if no input is provided
    class Meta:
        model = Account
        # metioning what the registration form will look like
        # All these fields will be visible in the form
        fields = ("first_name", "last_name", "email", "phone_no", "username", "password1", "password2")   



class cust_form(ModelForm):
    class Meta:
        model=Customer
        fields = ()   


# class LoginAuthenticationForm(forms.Form):
#     username=forms.CharField(label='username')
#     password=forms.CharField(label='password',widget=forms.PasswordInput)

    # class Meta:
    #     model=Account
    #     # metioning what the login form will look like
    #     # All these fields will be visible in the form
    #     fields=('username','password')

    #     # this is called before the form is submitted  
    #     def clean(self):
    #         username=self.cleaned_data['username']
    #         password=self.cleaned_data['password']
    #         if not authenticate(username=username, password=password):
    #             raise forms.ValidationError("Invalid login")
