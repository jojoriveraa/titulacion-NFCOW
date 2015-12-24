from django.db import models

# Create your models here.
class Mall(models.Model):
	id = models.PositiveIntegerField(primary_key=True)
	name = models.CharField(max_length = 255)
	address = models.CharField(max_length = 255)
	group = models.CharField(max_length = 255)
	image = models.ImageField(upload_to = 'malls')
	postcode = models.PositiveIntegerField()
	
	def __str__(self):
		return self.name