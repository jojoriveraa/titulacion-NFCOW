from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .forms import ProductForm
from .models import Product
from shopping_carts.models import Shopping_Cart
from userprofiles.models import CustomerProfile

# Create your views here.
def product_detail(request, id):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			id = id
			quantity = form.cleaned_data['quantity']
			q_customerprofile = CustomerProfile.objects.filter(user = request.user)[0]
			
			q1 = Shopping_Cart.objects.filter(customer__user = request.user)
			q2 = q1.filter(available = True)
			
			if not q2:
				q_shopping_cart = Shopping_Cart.objects.create_shopping_cart(date_time = timezone.now(), customer = q_customerprofile)
			else:
				q3 = q2.order_by('date_time').reverse()[0]
				q_shopping_cart = q2
			
			
			
			return render(request, 'test.html', {'id': id, 'quantity' : quantity, 'shopping_cart' : q_shopping_cart, })
			# return HttpResponseRedirect('/shopping-cart/1')
	else:
		form = ProductForm(request.POST or None)
		product = get_object_or_404(Product, id = id)
	
	return render(request, 'product.html', {'form' : form, 'product' : product, 'user' : request.user})