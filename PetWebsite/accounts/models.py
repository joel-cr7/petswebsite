from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError("Users must have username !!")
        if not email:
            raise ValueError("Users must have email !!")
        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

# class for custom user model
class Account(AbstractBaseUser):
    username = models.CharField(max_length=30, verbose_name='Username',unique=True)       
    email = models.CharField(max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)     
    last_login = models.DateTimeField(verbose_name='Last Login', auto_now=True)           
    is_active = models.BooleanField(default=True)                                         
    is_superuser = models.BooleanField(default=False)                                     
    is_staff = models.BooleanField(default=False)                                         
    is_admin = models.BooleanField(default=False)                                         
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=10)
    USERNAME_FIELD = 'username'        

    REQUIRED_FIELDS = [
        'email'
    ]    

    objects = MyAccountManager()   

    def __str__(self):      
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


