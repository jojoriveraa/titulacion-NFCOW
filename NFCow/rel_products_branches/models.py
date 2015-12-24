from django.db import models

from branches.models import Branch
from products.models import Product

# Create your models here.
class Rel_Product_Branch(models.Model):
	id_branch = models.ForeignKey(Branch)
	id_product = models.ForeignKey(Product)
	availability = models.NullBooleanField()
	
	def __str__(self):
		return self.id_branch + "-" + self.id_product