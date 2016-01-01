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
		
# class ProductListView(ListView):
# 	model = Product
# 	context_object_name = 'products'
# 	
# 	def get_template_names(self):
# 		return 'branch_list.html'
# 		
# 	def get_context_data(self, **kwargs):
# 		context = super(ProductListView, self).get_context_data(**kwargs)
# 		context['now'] = timezone.now()
# 		return context
# 		
# 	def get_queryset(self):
# 		return Product.objects.filter(branch_id = int(self.args[0]))