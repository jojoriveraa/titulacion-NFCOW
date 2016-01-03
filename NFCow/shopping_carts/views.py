from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.utils import timezone

from rel_products_shopping_carts.models import Rel_Product_Shopping_Cart
# Create your views here.

class ShoppingCartListView(ListView):
	model = Rel_Product_Shopping_Cart
	context_object_name = 'shopping_cart_products'
	
	def get_template_names(self):
		return 'shopping-cart.html'
		
	def get_context_data(self, **kwargs):
		context = super(ShoppingCartListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()	
		return context
		
	def get_queryset(self):
		return Rel_Product_Shopping_Cart.objects.filter(shopping_cart_id = int(self.args[0]))
	
	def multiply(value, arg):
		return value*arg