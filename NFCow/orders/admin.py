from django.contrib import admin

# Register your models here.
from .models import Order
from actions import export_as_excel

class OrderAdmin(admin.ModelAdmin):
		list_display = ('date_time', 'total', 'branch', 'user', 'status', )
		list_filter = ('date_time', )
		search_fields = ('date_time', 'user', )
		actions = (export_as_excel, )

admin.site.register(Order, OrderAdmin, )