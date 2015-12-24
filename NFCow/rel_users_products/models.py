from django.db import models

from products.models import Product
from users.models import User

# Create your models here.
class Rel_User_Product(models.Model):
	id_product = models.ForeignKey(Product)
	id_user = models.ForeignKey(User)
	dateTime = models.DateTimeField()

	def __str__(self):
		return self.id_product + "-" + self.id_user
	