from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import User

admin.site.site_header = "Folio Admin Panel"
admin.site.site_title = "Folio Admin Panel"
admin.site.index_title = "Welcome to the Folio Administration Panel!"


# Register your models here

class UserAdmin(UserAdmin):
    ordering = ('id',)
    list_display = [
        'id',
        'get_full_name',
        'first_name',
        'last_name',
        'username',
        'email',
        'image',
        'video',
        'birthday',
        'age',
        'is_active',
        'is_staff',
        'is_superuser',
        'date_joined',
        'last_login',   
    ]
    readonly_fields = (
        'id',
        'age',
        'last_login',
        "date_joined",
    )
    list_filter = (
        'first_name',
        'last_name',
        'username',
        'email',
        'birthday',
        'is_active',
        'is_staff',
        'is_superuser',
        'date_joined',
        'last_login',
    )
    search_fields = (
        'first_name',
        'last_name',
        'username',
        'email',
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password',)
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'bio', 'bio_1', 'image', 'video',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Important Dates', {
        'fields': ("date_joined", 'last_login', 'birthday', 'age',)
        }),
    )

admin.site.register(User, UserAdmin)
