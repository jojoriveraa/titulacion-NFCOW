from django.contrib import admin
from .models import Shopping_Cart

# Register your models here.

class Shopping_CartAdmin(admin.ModelAdmin):
		list_display = ('id', 'date_time', 'customer')
		list_filter = ('date_time', )

admin.site.register(Shopping_Cart, Shopping_CartAdmin)