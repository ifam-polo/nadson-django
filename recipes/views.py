from django.shortcuts import render

from utils.recipes.factory import make_recipe

from .models import Recipe  # Importação de recipes.models de Recipe.


def home(request):
    # Busca todas receitas criada em ordem id (cadastro) investida.
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,  # Busca as receitas criadas em admin.
    })


# Filtra os objetos de recipe por categoria pelo ID e pela ordem inversa.
def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        # Puxa as receitas cadastradas.
        'recipes': recipes,
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
