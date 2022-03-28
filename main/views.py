from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from .models import Cocktail, Cocktail_Base, Cocktail_Ingredient
from .serializers import MainSerializer, DetailSerializer, BaseSerializer, IngredientSerializer


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
    def get(self, request):
        try:
            data = {}
            cocktail = get_object_or_404(Cocktail, id=1) # 테스트로 id=1로 넣음
            detail = DetailSerializer(cocktail)
            data["info"] = detail.data

            print(Cocktail_Base.objects.all())
            bases_querysets = Cocktail_Base.objects.filter(cocktail=cocktail)
            print(bases_querysets)
            bases = BaseSerializer(bases_querysets, many=True)
            print(bases.data)
            data["bases"] = list(bases.data)

            ingredients_querysets = Cocktail_Ingredient.objects.filter(cocktail=cocktail)
            print(ingredients_querysets)
            ingredients = IngredientSerializer(ingredients_querysets, many=True)
            print(ingredients.data)
            data['ingredients'] = list(ingredients.data)

            return Response(data)

        except:
            return Response({"message": "error"})
