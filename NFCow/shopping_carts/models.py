from django.db import models
from userprofiles.models import CustomerProfile

# Create your models here.
class Shopping_CartManager(models.Manager):
	def create_shopping_cart(self, date_time, customer):
		shopping_cart = self.create(date_time = date_time, customer = customer)
		return shopping_cart
		
class Shopping_Cart(models.Model):
	date_time = models.DateTimeField()
	customer = models.ForeignKey(CustomerProfile)
	
	objects = Shopping_CartManager()
	
	def __str__(self):
		return self.customer.user.username + ' ; ' + self.date_time.strftime("%Y-%m-%d %H:%M:%S")
