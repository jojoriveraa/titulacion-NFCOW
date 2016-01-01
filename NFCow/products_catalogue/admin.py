from django.contrib import admin
from .models import Product_catalogue

# Register your models here.

class Product_catalogueAdmin(admin.ModelAdmin):
		list_display = ('name', 'description', 'img', )
		# list_filter = ('restaurant', 'mall', )
		# search_fields = ('restaurant', 'mall', )
		# list_editable = ('restaurant', 'mall', )
		
admin.site.register(Product_catalogue, Product_catalogueAdmin, )