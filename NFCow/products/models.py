from django.db import models
from products_catalogue.models import Product_catalogue

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length = 255)
	price = models.DecimalField(max_digits = 5, decimal_places = 2)
	discount = models.PositiveIntegerField(blank = True)
	product_super = models.ForeignKey(Product_catalogue)
	
	def img(self):
		return """
			<img src="%s" height="42"> 
		""" % self.product_super.image.url
		
	img.allow_tags = True
	
	def __str__(self):
		return self.name
