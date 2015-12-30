from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.EmailField(max_length = 255)
	image = models.ImageField(upload_to = 'malls')
	
	def img(self):
		return """
			<img src="%s" height="42"> 
		""" % self.image.url
		
	img.allow_tags = True
	
	def __str__(self):
		return self.first_name + ", " + self.last_name
	