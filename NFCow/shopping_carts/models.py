from django.db import models
from userprofiles.models import CustomerProfiles

# Create your models here.
class Shopping_Cart(models.Model):
	date_time = models.DateTimeField()
	customer = models.ForeignKey(CustomerProfiles)
	
	def __str__(self):
		return self.customer.user.username + ' ; ' + self.date_time.strftime("%Y-%m-%d %H:%M:%S")