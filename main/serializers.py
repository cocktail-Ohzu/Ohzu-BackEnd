from rest_framework import serializers
from .models import Cocktail, Cocktail_Base, Cocktail_Ingredient, Ingredient, Base, Mood, Weather, Ornament, Flavor


# 메인
class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = ['id', 'img', 'img2', 'background_color', 'name', 'eng_name', 'desc', 'strength']


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


# 검색 - Base
class SearchBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ['name', 'tag_color']


# 검색 - Ingredients
class SearchIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name', 'tag_color']


class DetailSerializer(serializers.ModelSerializer):
    flavors = FlavorSerializer(many=True, read_only=True)
    moods = MoodSerializer(many=True, read_only=True)
    weathers = WeatherSerializer(many=True, read_only=True)
    ornaments = OrnamentSerializer(many=True, read_only=True)

    class Meta:
        model = Cocktail
        fields = ['id', 'name', 'eng_name', 'background_color', 'img', 'img2', 'img3', 'desc', 'strength',
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
    desc = serializers.SerializerMethodField()

    def get_ingredient(self,obj):
        return obj.ingredient.name

    def get_tag_color(self, obj):
        return obj.ingredient.tag_color

    def get_desc(self, obj):
        return obj.ingredient.desc

    class Meta:
        model = Cocktail_Ingredient
        fields = ['ingredient', 'tag_color', 'amount', 'desc']


# 검색 api
class SearchSerializer(serializers.ModelSerializer):
    bases = SearchBaseSerializer(many=True, read_only=True)
    ingredients = SearchIngredientSerializer(many=True, read_only=True)
    # flavors = serializers.SerializerMethodField()
    # moods = serializers.SerializerMethodField()
    # ornaments = serializers.SerializerMethodField()
    # weathers = serializers.SerializerMethodField()
    flavors = FlavorSerializer(many=True, read_only=True)
    moods = MoodSerializer(many=True, read_only=True)
    weathers = WeatherSerializer(many=True, read_only=True)
    ornaments = OrnamentSerializer(many=True, read_only=True)

    # def get_bases(self, obj):
    #     return ", ".join([p.name for p in obj.bases.all()])
    #
    # def get_ingredients(self, obj):
    #     return ", ".join([p.name for p in obj.ingredients.all()])

    # def get_flavors(self, obj):
    #     return ", ".join([p.name for p in obj.flavors.all()])
    #
    # def get_moods(self, obj):
    #     return ", ".join([p.name for p in obj.moods.all()])
    #
    # def get_ingredients(self, obj):
    #     return ", ".join([p.name for p in obj.ingredients.all()])

    class Meta:
        model = Cocktail
        fields = ['id', 'name', 'eng_name', 'img', 'img2', 'img4', 'background_color',
                  'bases', 'ingredients', 'flavors', 'moods', 'weathers', 'ornaments']


# 맞춤 칵테일 추천
class RecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = ['id', 'name', 'img', 'img2', 'background_color']


# 추천 선택지 제공
class RecommendBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Base
        fields = ['id', 'name', 'tag_color', 'desc']


class RecommendIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'tag_color', 'desc', 'category']


class RecommendFlavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = ['id', 'name', 'tag_color']


class RecommendMoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = ['id', 'name', 'tag_color']


class RecommendWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['id', 'name', 'tag_color']


class RecommendOrnamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ornament
        fields = ['id', 'name', 'tag_color']