from django.db import models

from users.models import User
from branches.models import Branch

# Create your models here.
class Order(models.Model):
	dateTime = models.DateTimeField()
	total = models.DecimalField(max_digits = 5, decimal_places = 2)
	status = models.PositiveIntegerField()
	user = models.ForeignKey(User)
	branch = models.ForeignKey(Branch)
	
	def __str__(self):
		return self.id + "/" + self.user + "-" + self.branch