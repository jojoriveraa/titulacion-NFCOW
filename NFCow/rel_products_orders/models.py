from django.db import models

from orders.models import Order
from products.models import Product

# Create your models here.
class Rel_Product_Order(models.Model):
	order = models.ForeignKey(Order)
	product = models.ForeignKey(Product)
	
	def price(self):
		return self.product.price
	
	def __str__(self):
		return self.order.payment_date_time.strftime("%Y-%m-%d %H:%M:%S") + " ; " + self.order.user() + " ; " + self.product.name