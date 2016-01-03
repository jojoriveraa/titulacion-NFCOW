from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Rel_Product_Shopping_Cart

# Create your views here.
def product_remove(request, id, sc):
	product_in_shopping_cart = id
	shopping_cart_id = sc
	Rel_Product_Shopping_Cart.objects.filter(id = product_in_shopping_cart).delete()
	return HttpResponseRedirect('/shopping-cart/%s' % shopping_cart_id)