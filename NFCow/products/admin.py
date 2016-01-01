from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
		list_display = ('name', 'price', 'discount', 'img', )
		list_filter = ('product_super__name', )
		search_fields = ('name', )


admin.site.register(Product, ProductAdmin, )