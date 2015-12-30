from django.db import models

from products.models import Product
from users.models import User

# Create your models here.
class Rel_User_Product(models.Model):
	product = models.ForeignKey(Product)
	user = models.ForeignKey(User)
	date_time = models.DateTimeField()
	
	def user_name(self):
		return self.user.first_name + " " + self.user.last_name
	
	def __str__(self):
		return self.product.public_name + " ; " + self.user.first_name
	