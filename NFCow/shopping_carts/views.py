from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Shopping_Cart
from orders.models import Order
from rel_products_shopping_carts.models import Rel_Product_Shopping_Cart
from types_of_payment.models import TypeOfPayment
from django.contrib.auth.models import User
# Create your views here.

def cancel_shopping_cart(request):
	q_user = User.objects.filter(username = request.user)[0]
	Shopping_Cart.objects.create_shopping_cart(date_time = timezone.now(), user = q_user)
	return HttpResponseRedirect('/branches/1')

def pay_shopping_cart(request, total, sc_id, top_id):
	my_payment_date_time = timezone.now()
	my_total = total
	my_shopping_cart = Shopping_Cart.objects.filter(id = sc_id)[0]
	my_type_of_payment = TypeOfPayment.objects.filter(id = top_id)[0]
	order = Order.objects.create(payment_date_time = my_payment_date_time, total = my_total, shopping_cart = my_shopping_cart, type_of_payment = my_type_of_payment)
	q_user = User.objects.filter(user = request.user)[0]
	Shopping_Cart.objects.create_shopping_cart(date_time = timezone.now(), user = q_user)
	return HttpResponseRedirect('/order-detail/%s' % order.id)
	

class ShoppingCartListView(ListView):
	model = Rel_Product_Shopping_Cart
	context_object_name = 'shopping_cart_products'
	
	def get_template_names(self):
		return 'shopping-cart.html'
	
	def get_context_data(self, **kwargs):
		context = super(ShoppingCartListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		context['total'] = self.get_total()
		return context
	
	def get_queryset(self):
		return Rel_Product_Shopping_Cart.objects.filter(shopping_cart_id = int(self.args[0]))
	
	def get_total(self):
		products_in_sc = self.get_queryset()
		total = 0
		for scp in products_in_sc:
			total += scp.product.price * scp.quantity
		return total