from django.contrib import admin
from .models import Products

# Register your models here.


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("category", "sub_category", "name", "description", "img")


admin.site.register(Products, ProductsAdmin)
