from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userapp.models import HabrUser


# Register your models here.
class HabrUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets
    fieldsets[1][1]['fields'] = fieldsets[1][1]['fields'] + (
        'age', 'banned_until',
    )

    add_fieldsets = UserAdmin.add_fieldsets
    add_fieldsets[0][1]['fields'] = add_fieldsets[0][1]['fields'] + (
        'email', 'first_name', 'last_name', 'age',
    )

    list_display = ('username', 'first_name', 'last_name', 'email', 'age', 'is_active', 'banned_until')
    list_display_links = ('username',)
    search_fields = ('username', 'first_name', 'last_name', 'is_active')


admin.site.register(HabrUser, HabrUserAdmin)
