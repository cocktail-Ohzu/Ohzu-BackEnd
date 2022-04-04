from rest_framework import serializers
from .models import Cocktail, Cocktail_Base, Cocktail_Ingredient, Ingredient, Base, Mood, Weather, Ornament, Flavor


# 메인
class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = ['id', 'img', 'background_color', 'name', 'eng_name', 'desc', 'strength']


# 디테일
class TagListingField(serializers.RelatedField):

    def to_representation(self, value):
        return value.name


class DetailSerializer(serializers.ModelSerializer):
    flavors = TagListingField(many=True, read_only=True)
    moods = TagListingField(many=True, read_only=True)
    weathers = TagListingField(many=True, read_only=True)
    ornaments = TagListingField(many=True, read_only=True)

    class Meta:
        model = Cocktail
        fields = ['id', 'name', 'background_color', 'eng_name', 'img', 'desc', 'strength',
                  'flavors', 'moods', 'weathers', 'ornaments',
                  'recipe', 'ohzu_point']


class BaseSerializer(serializers.ModelSerializer):
    base = serializers.SerializerMethodField()
    desc = serializers.SerializerMethodField()

    def get_base(self, obj):
        return obj.base.name

    def get_desc(self, obj):
        return obj.base.desc

    class Meta:
        model = Cocktail_Base
        fields = ['base', 'desc', 'amount']


class IngredientSerializer(serializers.ModelSerializer):
    ingredient = serializers.SerializerMethodField()

    def get_ingredient(self,obj):
        return obj.ingredient.name

    class Meta:
        model = Cocktail_Ingredient
        fields = ['ingredient', 'amount']


# 검색 api
class SearchSerializer(serializers.ModelSerializer):
    bases = serializers.SerializerMethodField()
    flavors = serializers.SerializerMethodField()
    moods = serializers.SerializerMethodField()
    ornaments = serializers.SerializerMethodField()
    ingredients = serializers.SerializerMethodField()
    weathers = serializers.SerializerMethodField()

    def get_bases(self, obj):
        return ", ".join([p.name for p in obj.bases.all()])

    def get_flavors(self, obj):
        return ", ".join([p.name for p in obj.flavors.all()])

    def get_moods(self, obj):
        return ", ".join([p.name for p in obj.moods.all()])

    def get_ornaments(self, obj):
        return ", ".join([p.name for p in obj.ornaments.all()])

    def get_ingredients(self, obj):
        return ", ".join([p.name for p in obj.ingredients.all()])

    def get_weathers(self, obj):
        return ", ".join([p.name for p in obj.weathers.all()])


    class Meta:
        model = Cocktail
        fields = ['id', 'name', 'img', 'background_color',
                  'bases', 'flavors', 'moods', 'ornaments', 'ingredients', 'weathers']