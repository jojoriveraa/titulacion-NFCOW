from django.contrib import admin

# Register your models here.
from .models import Rel_Product_Order

# class Rel_Product_OrderAdmin(admin.ModelAdmin):
# 		list_display = ('order', 'product', 'price',  )
# 		list_filter = ('order__date_time', 'product',  )

admin.site.register(Rel_Product_Order)