from django.contrib import admin

from .models import ItemModel


@admin.register(ItemModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
