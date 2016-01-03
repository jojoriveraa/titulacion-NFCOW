from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Shopping_Cart
from rel_products_shopping_carts.models import Rel_Product_Shopping_Cart
from userprofiles.models import CustomerProfile
# Create your views here.

def cancel_shopping_cart(request):
	q_customerprofile = CustomerProfile.objects.filter(user = request.user)[0]
	Shopping_Cart.objects.create_shopping_cart(date_time = timezone.now(), customer = q_customerprofile)
	return HttpResponseRedirect('/branches/1')

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