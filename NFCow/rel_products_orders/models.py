from django.db import models

from orders.models import Order
from products.models import Product

# Create your models here.
class Rel_Product_Order(models.Model):
	id_order = models.ForeignKey(Order)
	id_product = models.ForeignKey(Product)
	price_article = models.DecimalField(max_digits = 5, decimal_places = 2)
	quantity = models.PositiveIntegerField()
	
	def __str__(self):
		return self.id_order + "-" + self.id_product