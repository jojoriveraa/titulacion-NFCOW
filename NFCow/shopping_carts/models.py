from django.db import models
from users.models import User
from userprofiles.models import CustomerProfiles

# Create your models here.
class Shopping_Cart(models.Model):
	date_time = models.DateTimeField()
	user = models.ForeignKey(User)
	customer = models.ForeignKey(CustomerProfiles)
	
	def __str__(self):
		return self.user.first_name + ' ; ' + self.date_time.strftime("%Y-%m-%d %H:%M:%S")