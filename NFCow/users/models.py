from django.db import models

# Create your models here.
class User(models.Model):
	fistr_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email = models.EmailField(max_length = 255)
	image = models.ImageField(upload_to = 'malls')
	type = models.PositiveIntegerField()
	
	def __str__(self):
		return self.fistr_name + ", " + self.last_name
	