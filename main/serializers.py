from rest_framework import serializers
from .models import Cocktail, Cocktail_Base, Cocktail_Ingredient, Ingredient, Base


# 메인
class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = ['id', 'img', 'name', 'eng_name', 'desc', 'strength']


# 디테일
class TagListingField(serializers.RelatedField):

    def to_representation(self, value):
        return value.name


class DetailSerializer(serializers.ModelSerializer):
    flavors = TagListingField(many=True, read_only=True)
    moods = TagListingField(many=True, read_only=True)
    weathers = TagListingField(many=True, read_only=True)
    ornaments = TagListingField(many=True, read_only=True)

    # def get_flavors(self, obj):
    #     return obj.get_flavors()
    #
    # def get_moods(self, obj):
    #     return obj.get_moods()
    #
    # def get_weathers(self, obj):
    #     return obj.get_weathers()
    #
    # def get_ornaments(self, obj):
    #     return obj.get_ornaments()

    class Meta:
        model = Cocktail
        fields = ['id', 'name', 'eng_name', 'img', 'desc', 'strength',
                  'flavors', 'moods', 'weathers', 'ornaments',
                  'recipe']


class BaseSerializer(serializers.ModelSerializer):
    base = serializers.SerializerMethodField()

    def get_base(self, obj):
        return obj.base.name

    class Meta:
        model = Cocktail_Base
        fields = ['base', 'amount']


class IngredientSerializer(serializers.ModelSerializer):
    ingredient = serializers.SerializerMethodField()

    def get_ingredient(self,obj):
        return obj.ingredient.name

    class Meta:
        model = Cocktail_Ingredient
        fields = ['ingredient', 'amount']