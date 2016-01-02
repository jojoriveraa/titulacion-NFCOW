from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login

from .forms import ProductForm
from .models import Product

# Create your views here.
def product_detail(request, id):
	form = ProductForm(request.POST or None)
	
	product = get_object_or_404(Product, id = id)
	
	# if form.is_valid():
	# 	form.save()
	
	return render(request, 'product.html', {'form' : form, 'product' : product})