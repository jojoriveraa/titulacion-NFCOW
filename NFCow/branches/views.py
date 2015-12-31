from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.utils import timezone

from .models import Branch
# Create your views here.

class BranchDetailView(DetailView):
	model = Branch
	context_object_name = 'branch'
	
	def get_template_names(self):
		return 'branches.html'

class BranchListView(ListView):
	model = Branch
	
	model.allow_tags = True
	
	context_object_name = 'branches'
	
	def get_template_names(self):
		return 'branch_list.html'
		
	def get_context_data(self, **kwargs):
		context = super(BranchListView, self).get_context_data(**kwargs)
		context['now'] = timezone.now()
		return context