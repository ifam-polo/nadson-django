from django.contrib import admin

# Register your models here.
from .models import Category


# classe categoria criada para a classe administrativa do model.Ela herda da classe ModelAdmin.
class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
