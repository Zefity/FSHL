from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Thing

admin.site.register(Category)
admin.site.register(Thing)