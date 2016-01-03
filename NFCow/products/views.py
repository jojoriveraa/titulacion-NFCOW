from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import ProductForm
from .models import Product

# Create your views here.
def product_detail(request, id):
	if request.method == 'POST':
		# if form.is_valid():
		# 	form.save()
		return HttpResponseRedirect('/shopping-cart/1')
	else:
		form = ProductForm(request.POST or None)
		product = get_object_or_404(Product, id = id)
		return render(request, 'product.html', {'form' : form, 'product' : product})