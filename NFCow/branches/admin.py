from django.contrib import admin

# Register your models here.
from .models import Branch

class BranchAdmin(admin.ModelAdmin):
		list_display = ('name', 'restaurant', 'imgRestaurant', 'mall', 'imgMall', )
		list_filter = ('restaurant', 'mall', )
		search_fields = ('restaurant', 'mall', )
		list_editable = ('restaurant', 'mall', )

admin.site.register(Branch, BranchAdmin, )