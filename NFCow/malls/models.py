from django.db import models

# Create your models here.
class Mall(models.Model):
	name = models.CharField(max_length = 255)
	address = models.CharField(max_length = 255)
	group = models.CharField(max_length = 255)
	image = models.ImageField(upload_to = 'malls')
	postcode = models.PositiveIntegerField()
	
	def img(self):
		return """
			<img src="%s" height="42" width="42"> 
		""" % self.image.url
	
	img.allow_tags = True
	img.admin_order_field = 'image'
	
	def __str__(self):
		return self.name