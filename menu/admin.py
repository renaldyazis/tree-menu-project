from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu_name', 'parent', 'order')
    list_filter = ('menu_name',)
    search_fields = ('name', 'url', 'named_url')
    fields = ('name', 'menu_name', 'url', 'named_url', 'parent', 'order')
    ordering = ('menu_name', 'order')


admin.site.register(MenuItem, MenuItemAdmin)
