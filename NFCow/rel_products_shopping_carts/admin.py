from django.contrib import admin
from .models import Rel_Product_Shopping_Cart

# Register your models here.
# class Rel_Product_Shopping_CartAdmin(admin.ModelAdmin):
# 		list_display = ('id', 'date_time', 'user', )
# 		list_filter = ('date_time', )

admin.site.register(Rel_Product_Shopping_Cart)