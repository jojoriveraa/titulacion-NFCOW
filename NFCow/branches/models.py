from django.db import models

from restaurants.models import Restaurant
from malls.models import Mall

# Create your models here.
class Branch(models.Model):
	id = models.PositiveIntegerField(primary_key=True)
	name = models.CharField(max_length = 255)
	restaurant = models.ForeignKey(Restaurant)
	mall = models.ForeignKey(Mall)
	
	def __str__(self):
		return self.name