from django.db import models
from categories.models import Category
from restaurants.models import Restaurant

# Create your models here.
class Product_catalogue(models.Model):
	name = models.CharField(max_length = 255)
	description = models.TextField(blank = True)
	image = models.ImageField(upload_to = 'products_catalogue')
	categories = models.ManyToManyField('categories.Category', blank = True, related_name = 'products_category',)
	restaurant = models.ForeignKey(Restaurant, blank = True)
	
	def img(self):
		return """
			<img src="%s" height="42"> 
		""" % self.image.url
	
	img.allow_tags = True
	
	def __str__(self):
		return self.name