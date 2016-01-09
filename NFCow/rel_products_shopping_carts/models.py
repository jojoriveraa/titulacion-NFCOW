from django.db import models
from products.models import Product
from shopping_carts.models import Shopping_Cart

# Create your models here.
class Rel_Product_Shopping_Cart(models.Model):
	product = models.ForeignKey(Product)
	quantity = models.IntegerField()
	shopping_cart = models.ForeignKey(Shopping_Cart)
	
	def __str__(self):
		return self.shopping_cart.date_time.strftime("%Y-%m-%d %H:%M:%S") + ' ; ' + self.shopping_cart.user.username + ' ; ' + self.product.name