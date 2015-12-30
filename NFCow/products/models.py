from django.db import models

# Create your models here.
class Product(models.Model):
	public_name = models.CharField(max_length = 255)
	private_name = models.CharField(max_length = 255)
	price = models.DecimalField(max_digits = 5, decimal_places = 2)
	discount = models.PositiveIntegerField(blank = True)
	image = models.ImageField(upload_to = 'products')
	
	def img(self):
		return """
			<img src="%s" height="42"> 
		""" % self.image.url
	
	img.allow_tags = True
	img.admin_order_field = 'image'
	
	def __str__(self):
		return self.private_name
