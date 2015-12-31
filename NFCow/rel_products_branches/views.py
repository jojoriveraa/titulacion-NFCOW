from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.utils import timezone

from .models import Rel_Product_Branch
# Create your views here.

class ProductInBranchListView(ListView):
	
	model = Rel_Product_Branch
	context_object_name = 'products_in_branch'
	# branch_id = 
	# queryset = Rel_Product_Branch.objects.filter(branch_id = )
	
	def get_template_names(self):
		return 'products-in-branch.html'
		
	def get_context_data(self, **kwargs):
		context = super(ProductInBranchListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context

	def get_queryset(self):
		return Rel_Product_Branch.objects.filter(branch_id = int(self.args[0]))