from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length = 255)
	style = models.CharField(max_length = 255)
	image = models.ImageField(upload_to = 'restaurants')
	
	def img(self):
		return """
			<img src="%s" height="42"> 
		""" % self.image.url
	
	img.allow_tags = True
	img.admin_order_field = 'image'
	
	def __str__(self):
		return self.name
	