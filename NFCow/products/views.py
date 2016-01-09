from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .forms import ProductForm
from .models import Product
from shopping_carts.models import Shopping_Cart
from django.contrib.auth.models import User
from rel_products_shopping_carts.models import Rel_Product_Shopping_Cart

# Create your views here.
def product_detail(request, id):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			q_product = Product.objects.filter(id = id)[0]
			q_quantity = form.cleaned_data['quantity']
			q_user = User.objects.filter(username = request.user)[0]
			
			q1 = Shopping_Cart.objects.filter(user = request.user)
			q2 = q1.filter(available = True)
			
			if not q2:
				q_shopping_cart = Shopping_Cart.objects.create_shopping_cart(date_time = timezone.now(), user = q_user)
			else:
				q3 = q2.order_by('date_time').reverse()[0]
				q_shopping_cart = q3
			
			shc_id = q_shopping_cart.id
			Rel_Product_Shopping_Cart.objects.create(product = q_product, quantity = q_quantity, shopping_cart = q_shopping_cart)
			
			return HttpResponseRedirect('/shopping-cart/%s' % shc_id)
	else:
		form = ProductForm(request.POST or None)
		product = get_object_or_404(Product, id = id)
	
	return render(request, 'product.html', {'form' : form, 'product' : product, 'q_user' : request.user})