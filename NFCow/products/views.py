from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import FormMixin

from django.utils import timezone

from .models import Product
from .forms import ProductForm
# Create your views here.

class ProductDetailView(FormMixin, DetailView):
	model = Product
	context_object_name = 'product'
	form_class = ProductForm
	
	def get_template_names(self):
		return 'product.html'

	def get_context_data(self, **kwargs):
		context = super(ProductDetailView, self).get_context_data(**kwargs)
		context['form'] = ProductForm()
		context['now'] = timezone.now()
		return context