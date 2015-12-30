from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
		list_display = ('public_name', 'private_name', 'price', 'discount', 'img', )
		list_filter = ('public_name', )
		search_fields = ('public_name', 'private_name', )


admin.site.register(Product, ProductAdmin, )