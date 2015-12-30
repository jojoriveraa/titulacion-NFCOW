from django.contrib import admin

# Register your models here.
from .models import Rel_User_Product

class Rel_User_ProductAdmin(admin.ModelAdmin):
		list_display = ('date_time', 'product', 'user_name', )
		list_filter = ('date_time', )
		search_fields = ('date_time', 'user', )

admin.site.register(Rel_User_Product, Rel_User_ProductAdmin, )