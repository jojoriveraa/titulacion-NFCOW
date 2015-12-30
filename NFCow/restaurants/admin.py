from django.contrib import admin

# Register your models here.
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
		list_display = ('name', 'style', 'img', )
		search_fields = ('name', 'style', )

admin.site.register(Restaurant, RestaurantAdmin)