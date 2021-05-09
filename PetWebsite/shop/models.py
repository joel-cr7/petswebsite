from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()
# Create your models here.

class Product(models.Model):     #please not when ever u create a model, register it to the admin of that app or file
    product_id=models.AutoField
    product_name=models.CharField(max_length=30)
    category=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    our_price=models.IntegerField(default=0)
    images=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name


class Customer(models.Model):
	user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])   #calculating final total for all orderitems
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 



class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.our_price * self.quantity  #calculating total price for each item based on the quantity
		return total