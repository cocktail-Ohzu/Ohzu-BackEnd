from django.contrib import admin
from .models import Cocktail, Cocktail_Ingredient, Ingredient


class Cocktail_Ingredient_Inline(admin.TabularInline):
    model = Cocktail_Ingredient


@admin.register(Cocktail)
class PlanAdmin(admin.ModelAdmin):
    inlines = [Cocktail_Ingredient_Inline]


@admin.register(Ingredient)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc']
    list_display_links = ['id', 'name']
