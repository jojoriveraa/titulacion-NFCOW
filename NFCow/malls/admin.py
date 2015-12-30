from django.contrib import admin

# Register your models here.
from .models import Mall

class MallAdmin(admin.ModelAdmin):
		list_display = ('name', 'img', 'postcode', )
		list_filter = ('name', )
		search_fields = ('name', 'postcode', )

admin.site.register(Mall, MallAdmin, )