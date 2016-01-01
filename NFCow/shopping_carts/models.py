from django.db import models
from users.models import User

# Create your models here.
class Shopping_Cart(models.Model):
	date_time = models.DateTimeField()
	user = models.ForeignKey(User)
	
	def __str__(self):
		return self.user.first_name + ' ; ' + self.date_time.strftime("%Y-%m-%d %H:%M:%S")