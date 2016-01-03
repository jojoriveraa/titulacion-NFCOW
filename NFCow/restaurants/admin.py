from django.contrib import admin

# Register your models here.
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
		list_display = ('name', 'img', )
		filter_horizontal = ('categories', )
		search_fields = ('name', )

admin.site.register(Restaurant, RestaurantAdmin)