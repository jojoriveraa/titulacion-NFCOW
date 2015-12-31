from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.utils import timezone

from .models import Product
# Create your views here.

class ProductDetailView(DetailView):
	model = Product
	context_object_name = 'product'
	
	def get_template_names(self):
		return 'product.html'