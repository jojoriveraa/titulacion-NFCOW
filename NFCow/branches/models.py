from django.db import models

from restaurants.models import Restaurant
from malls.models import Mall

# Create your models here.
class Branch(models.Model):
	name = models.CharField(max_length = 255)
	restaurant = models.ForeignKey(Restaurant)
	mall = models.ForeignKey(Mall)
	
	def imgRestaurant(self):
		return """
			<img src="%s" height="42"> 
		""" % self.restaurant.image.url
	
	def imgMall(self):
		return """
			<img src="%s" height="42"> 
		""" % self.mall.image.url
	
	imgRestaurant.allow_tags = True
	imgMall.allow_tags = True
	
	def __str__(self):
		return self.name