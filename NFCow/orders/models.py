from django.db import models

from shopping_carts.models import Shopping_Cart
from types_of_payment.models import TypeOfPayment

# Create your models here.
class Order(models.Model):
	payment_date_time = models.DateTimeField()
	total = models.CharField(max_length = 7)
	shopping_cart = models.ForeignKey(Shopping_Cart)
	type_of_payment = models.ForeignKey(TypeOfPayment)
	
	def user(self):
		return self.shopping_cart.user.username

	def __str__(self):
		return self.payment_date_time.strftime("%Y-%m-%d %H:%M:%S") + " ; " + self.shopping_cart.user.username