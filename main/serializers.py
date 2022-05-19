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


# 맛
class FlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = ['name', 'tag_color']


# 무드
class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ['name', 'tag_color']


# 날씨 / 계절
class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['name', 'tag_color']


# 장식
class OrnamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ornament
        fields = ['name', 'tag_color']


class DetailSerializer(serializers.ModelSerializer):
    flavors = FlavorSerializer(many=True, read_only=True)
    moods = MoodSerializer(many=True, read_only=True)
    weathers = WeatherSerializer(many=True, read_only=True)
    ornaments = OrnamentSerializer(many=True, read_only=True)

    class Meta:
        model = Cocktail
        fields = ['id', 'name', 'eng_name', 'background_color', 'eng_name', 'img', 'desc', 'strength',
                  'flavors', 'moods', 'weathers', 'ornaments',
                  'recipe', 'ohzu_point']


class BaseSerializer(serializers.ModelSerializer):
    base = serializers.SerializerMethodField()
    desc = serializers.SerializerMethodField()
    tag_color = serializers.SerializerMethodField()

    def get_base(self, obj):
        return obj.base.name

    def get_desc(self, obj):
        return obj.base.desc

    def get_tag_color(self, obj):
        return obj.base.tag_color

    class Meta:
        model = Cocktail_Base
        fields = ['base', 'tag_color', 'desc']


class IngredientSerializer(serializers.ModelSerializer):
    ingredient = serializers.SerializerMethodField()
    tag_color = serializers.SerializerMethodField()

    def get_ingredient(self,obj):
        return obj.ingredient.name

    def get_tag_color(self, obj):
        return obj.ingredient.tag_color

    class Meta:
        model = Cocktail_Ingredient
        fields = ['ingredient', 'tag_color', 'amount']


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