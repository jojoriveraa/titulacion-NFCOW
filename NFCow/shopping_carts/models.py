from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shopping_CartManager(models.Manager):
	def create_shopping_cart(self, date_time, user):
		self.filter(user = user).update(available = False)
		shopping_cart = self.create(date_time = date_time, user = user, available = True)
		return shopping_cart
		
class Shopping_Cart(models.Model):
	date_time = models.DateTimeField()
	user = models.ForeignKey(User)
	available = models.NullBooleanField()
	
	objects = Shopping_CartManager()
	
	def __str__(self):
		return self.user.username + ' ; ' + self.date_time.strftime("%Y-%m-%d %H:%M:%S")
