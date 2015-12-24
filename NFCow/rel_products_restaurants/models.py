from django.db import models

from products.models import Product
from restaurants.models import Restaurant

# Create your models here.
class Rel_Product_Restaurant(models.Model):
	id_product = models.ForeignKey(Product)
	id_restaurant = models.ForeignKey(Restaurant)
	
	def __str__(self):
		return self.id_product + "-" + self.id_restaurant
	