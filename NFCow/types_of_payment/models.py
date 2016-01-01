from django.db import models

# Create your models here.
class TypeOfPayment(models.Model):
	type_of_payment = models.CharField(max_length = 255)
	
	def __str__(self):
		return self.type_of_payment