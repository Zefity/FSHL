from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category"]


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Review)
admin.site.register(models.CartThing)
admin.site.register(models.Cart)
admin.site.register(models.Customer)
admin.site.register(models.Thing)