from django.contrib import admin

# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
		list_display = ('last_name', 'first_name', 'img', )
		search_fields = ('last_name', 'first_name', 'email', )

admin.site.register(User, UserAdmin, )