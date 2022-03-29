from rest_framework import serializers
from .models import Cocktail, Cocktail_Base, Cocktail_Ingredient, Ingredient, Base, Mood, Weather, Ornament, Flavor


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

    class Meta:
        model = Cocktail
        fields = ['id', 'name', 'eng_name', 'img', 'desc', 'strength',
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