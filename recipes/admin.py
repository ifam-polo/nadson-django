from django.contrib import admin

# Register your models here.
from .models import Category, Recipe


# classe catego. criada para a classe adminis. do model. herda da clss modeladm. # noqa:E501
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
