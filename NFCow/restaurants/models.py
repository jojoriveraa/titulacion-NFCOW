from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length = 255)
	type = models.CharField(max_length = 255)
	image = models.ImageField(upload_to = 'restaurants')
	
	def __str__(self):
		return self.name
	