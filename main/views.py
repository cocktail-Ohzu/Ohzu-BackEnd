from collections import defaultdict

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from .models import Cocktail, Cocktail_Base, Cocktail_Ingredient, Cocktail_Flavor
from .serializers import MainSerializer, DetailSerializer, BaseSerializer, IngredientSerializer, SearchSerializer


# 메인 화면
class MainCocktailView(APIView):
    def get(self, request):
        today = datetime.today()
        today_cocktail = (today.year + today.month + today.day) % 36  # 오늘의 추천 칵테일 랜덤
        cocktail = get_object_or_404(Cocktail, id=today_cocktail+1)
        serializer = MainSerializer(cocktail)
        return Response(serializer.data)


# 상세 페이지
class DetailCocktailView(APIView):
    def get(self, request, id):
        try:
            data = {}
            cocktail = get_object_or_404(Cocktail, id=id)
            detail = DetailSerializer(cocktail)
            data["info"] = detail.data

            bases_querysets = Cocktail_Base.objects.filter(cocktail=cocktail)
            bases = BaseSerializer(bases_querysets, many=True)
            data["bases"] = list(bases.data)

            ingredients_querysets = Cocktail_Ingredient.objects.filter(cocktail=cocktail)
            ingredients = IngredientSerializer(ingredients_querysets, many=True)
            data['ingredients'] = list(ingredients.data)

            return Response(data)

        except:
            return Response({"message": "error"})


# 검색 api
class SearchTagView(APIView):
    def get(self, request):
        try:
            cocktails = Cocktail.objects.all()
            serializer = SearchSerializer(cocktails, many=True)
            return Response(serializer.data)
        except:
            return Response({"message": "error"})


# 추천 페이지
class RecommendView(APIView):
    def get(self, request):
        try:
            result_cocktail = []
            data = defaultdict(list)

            id_list = list(request.data)

            for tag_id in id_list:
                if tag_id == 'base_id':
                    base_cocktail = []
                    bases = Cocktail_Base.objects.filter(base_id=request.data['base_id'])

                    for base in bases:
                        result_cocktail.append(base.cocktail_id)
                        base_cocktail.append(base.cocktail_id)

                    data['base'] += base_cocktail

                elif tag_id == 'ingredient_id':
                    ingredient_cocktail = []
                    ingredients = Cocktail_Ingredient.objects.filter(ingredient_id=request.data['ingredient_id'])

                    for ingredient in ingredients:
                        result_cocktail.append(ingredient.cocktail)
                        ingredient_cocktail.append(ingredient.cocktail)

                    data['ingredient'] += ingredient_cocktail

            return Response(data, status=status.HTTP_200_OK)

        except:
            return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)