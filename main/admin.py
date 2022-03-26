from django.contrib import admin
from .models import Cocktail, Base, Flavor, Mood, Ornament, Ingredient, Weather, Cocktail_Ingredient, Cocktail_Base


@admin.register(Base)
class BaseAdmin(admin.ModelAdmin):
    pass


@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    pass


@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    pass


@admin.register(Ornament)
class MoodAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    pass


@admin.register(Cocktail)
class CocktailAdmin(admin.ModelAdmin):
    filter_horizontal = ('bases', 'flavors', 'moods', 'ornaments', 'ingredients', 'weathers',)
    list_display = ['id', 'name', 'eng_name', 'img', 'background_color', 'desc', 'strength', 'cocktail_color', 'recipe', 'ohzu_point',
                    'get_bases', 'get_flavors', 'get_moods', 'get_ornaments', 'get_ingredients', 'get_weathers']


@admin.register(Cocktail_Ingredient)
class Cocktail_IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'cocktail', 'ingredient', 'amount']


@admin.register(Cocktail_Base)
class Cocktail_BaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'cocktail', 'base', 'amount']