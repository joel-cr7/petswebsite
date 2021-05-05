from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
# class customUser(models.Model):
#     phone_no=models.CharField(max_length=10)
#     email=models.CharField(max_length=30)
#     user=models.OneToOneField(User,on_delete=models.CASCADE)


# class for custom user model manager
class MyAccountManager(BaseUserManager):
    # compulsory to override two methods
    def create_user(self, username, email, password=None):
        # validation
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
    username = models.CharField(max_length=30, verbose_name='Username',unique=True)       # compulsory to mention
    email = models.CharField(max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)     # compulsory to mention
    last_login = models.DateTimeField(verbose_name='Last Login', auto_now=True)           # compulsory to mention
    is_active = models.BooleanField(default=True)                                         # compulsory to mention
    is_superuser = models.BooleanField(default=False)                                     # compulsory to mention
    is_staff = models.BooleanField(default=False)                                         # compulsory to mention
    is_admin = models.BooleanField(default=False)                                         # compulsory to mention
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=10)

    # whatever user will be able to login with
    USERNAME_FIELD = 'username'        

    # mention all required fields which will be needed during register (username is by default required)
    REQUIRED_FIELDS = [
        'email'
    ]    

    objects = MyAccountManager()    # using the custom manager

    def __str__(self):       # what to display when we use account object in template 
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


