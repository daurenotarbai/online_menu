from django.contrib import admin
from menu_app import models

class RestaurantAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Restaurant._meta.fields]

admin.site.register(models.Restaurant, RestaurantAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Product._meta.fields]

admin.site.register(models.Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Category._meta.fields]


admin.site.register(models.Category, CategoryAdmin)
