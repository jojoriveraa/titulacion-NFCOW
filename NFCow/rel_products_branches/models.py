from django.db import models

from branches.models import Branch
from products.models import Product

# Create your models here.
class Rel_Product_Branch(models.Model):
	branch = models.ForeignKey(Branch)
	product = models.ForeignKey(Product)
	availability = models.NullBooleanField()
	
	def __str__(self):
		return self.product.public_name + " ; " + self.branch.name