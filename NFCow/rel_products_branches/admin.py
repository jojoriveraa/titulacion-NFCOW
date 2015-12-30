from django.contrib import admin

# Register your models here.
from .models import Rel_Product_Branch

class Rel_Product_BranchAdmin(admin.ModelAdmin):
		list_display = ('branch', 'product', 'availability',  )
		list_filter = ('branch', 'product',  )
		search_fields = ('branch', 'product',  )
		list_editable = ('product', 'availability', )
		
admin.site.register(Rel_Product_Branch, Rel_Product_BranchAdmin, )
