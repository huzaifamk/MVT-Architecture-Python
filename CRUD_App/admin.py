from django.contrib import admin
from CRUD_App.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',
                    'user_name', 'email', 'password')
    search_fields = ('first_name', 'last_name',
                     'user_name', 'email', 'password')
    list_per_page = 50


admin.site.register(User, UserAdmin)
