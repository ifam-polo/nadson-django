from django.shortcuts import render

from utils.recipes.factory import make_recipe

from .models import Recipe  # Importação de recipes.models de Recipe.


def home(request):
    # Busca todas receitas criada em ordem id (cadastro) investida.
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,  # Busca as receitas criadas em admin.
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        # Define a quantidade de receitas por página.
        'recipes': recipes,
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
