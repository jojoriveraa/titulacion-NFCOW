from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone

from orders.models import Order
from rel_products_shopping_carts.models import Rel_Product_Shopping_Cart

class OrderDetailView(DetailView):
	model = Order
	context_object_name = 'order'
	
	def get_template_names(self):
		return 'order-detail.html'
	
	def get_context_data(self, **kwargs):
		context = super(OrderDetailView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		context['products'] = Rel_Product_Shopping_Cart.objects.filter(shopping_cart_id = self.kwargs['pk'])
		return context

class OrderListView(ListView):
	model = Order
	context_object_name = 'orders'
	
	def get_template_names(self):
		return 'order-list.html'
	
	def get_context_data(self, **kwargs):
		context = super(OrderListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context
	
	def get_queryset(self):
		return Order.objects.filter(shopping_cart__customer__user = self.request.user)