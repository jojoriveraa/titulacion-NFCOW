from django.db import models
from categories.models import Category

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length = 255)
	image = models.ImageField(upload_to = 'restaurants')
	categories = models.ManyToManyField('categories.Category', blank = True, related_name = 'restaurants_category',)
	
	def img(self):
		return """
			<img src="%s" height="42"> 
		""" % self.image.url
	
	img.allow_tags = True
	img.admin_order_field = 'image'
	
	def __str__(self):
		return self.name
	