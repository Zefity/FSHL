from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Thing

admin.site.register(Category)


@admin.register(Thing)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')
