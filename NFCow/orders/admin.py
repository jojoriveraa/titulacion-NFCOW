from django.contrib import admin

# Register your models here.
from .models import Order
from actions import export_as_excel

class OrderAdmin(admin.ModelAdmin):
		list_display = ('shopping_cart', 'payment_date_time', 'total', 'type_of_payment', 'user')
		list_filter = ('payment_date_time', )
		search_fields = ('payment_date_time', 'shopping_cart__user__first_name',)
		actions = (export_as_excel, )

admin.site.register(Order, OrderAdmin, )