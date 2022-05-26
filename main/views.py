from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from .models import Cocktail, Cocktail_Base, Cocktail_Ingredient, Cocktail_Flavor, Cocktail_Mood, Cocktail_Weather, \
    Cocktail_Ornament, Flavor
from .serializers import MainSerializer, DetailSerializer, BaseSerializer, IngredientSerializer, SearchSerializer, \
    RecommendSerializer


# 메인 화면
class MainCocktailView(APIView):
    def get(self, request):
        today = datetime.today()
        today_cocktail = (today.year + today.month + today.day) % 36  # 오늘의 추천 칵테일 랜덤
        cocktail = get_object_or_404(Cocktail, id=today_cocktail + 1)
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
            # 딱 맞는 결과가 없을 경우, 빈도가 가장 많은, 유사한 칵테일을 추천하기 위한 리스트
            result_cocktail = []
            # 알맞는 칵테일을 추천하기 위한 리스트
            data = []

            # 유저가 추천 받고자 하는 필드 저장
            id_list = list(request.data)

            for tag_id in id_list:

                # 베이스 추천
                if tag_id == 'base_id':
                    base_cocktail = []

                    for i in request.data['base_id']:
                        bases = Cocktail_Base.objects.filter(base_id=i)

                        for base in bases:
                            result_cocktail.append(base.cocktail_id)
                            base_cocktail.append(base.cocktail_id)

                    data.append(base_cocktail)
                    continue

                # 재료 추천
                if tag_id == 'ingredient_id':
                    ingredient_cocktail = []

                    for i in request.data['ingredient_id']:
                        ingredients = Cocktail_Ingredient.objects.filter(ingredient_id=i)

                        for ingredient in ingredients:
                            result_cocktail.append(ingredient.cocktail_id)
                            ingredient_cocktail.append(ingredient.cocktail_id)

                    data.append(ingredient_cocktail)
                    continue

                # 맛 추천
                if tag_id == 'flavor_id':
                    flavor_cocktail = []

                    for i in request.data['flavor_id']:
                        flavors = Cocktail_Flavor.objects.filter(flavor_id=i)

                        for flavor in flavors:
                            result_cocktail.append(flavor.cocktail_id)
                            flavor_cocktail.append(flavor.cocktail_id)

                    data.append(flavor_cocktail)
                    continue

                # 무드/기분 추천
                if tag_id == 'mood_id':
                    mood_cocktail = []

                    for i in request.data['mood_id']:
                        moods = Cocktail_Mood.objects.filter(mood_id=i)

                        for mood in moods:
                            result_cocktail.append(mood.cocktail_id)
                            mood_cocktail.append(mood.cocktail_id)

                    data.append(mood_cocktail)
                    continue

                # 날씨/계절 추천
                if tag_id == 'weather_id':
                    weather_cocktail = []

                    for i in request.data['weather_id']:
                        weathers = Cocktail_Weather.objects.filter(weather_id=i)

                        for weather in weathers:
                            result_cocktail.append(weather.cocktail_id)
                            weather_cocktail.append(weather.cocktail_id)

                    data.append(weather_cocktail)
                    continue

                # 가니쉬 추천
                if tag_id == 'ornament_id':
                    ornament_cocktail = []

                    for i in request.data['ornament_id']:
                        ornaments = Cocktail_Ornament.objects.filter(ornament_id=i)

                        for ornament in ornaments:
                            result_cocktail.append(ornament.cocktail_id)
                            ornament_cocktail.append(ornament.cocktail_id)

                    data.append(ornament_cocktail)
                    continue

                # 도수 추천
                            result_cocktail.append(ornament.cocktail_id)
                            ornament_cocktail.append(ornament.cocktail_id)

                    data.append(ornament_cocktail)
                    continue

            # 유사한 칵테일 id 리스트
            similar_result = []

            # 조건을 모두 만족 시키는 칵테일 id 리스트
            fit_result = []

            # 사용자가 선택한 필드들에 맞는 칵테일 빈도수 높은 순으로 정렬
            result_cocktail.sort(key=lambda x: result_cocktail.count(x))
            result = list(set(result_cocktail))

            # 사용자가 선택한 필드들을 모두 만족하는 칵테일 얻기 위한 교집합 intersection 변수
            intersection = list(set(data[0]))

            # data에 담긴 리스트들을 돌면서 교집합 확인
            for i in range(1, len(data)):
                intersection = list((set(intersection) & set(data[i])))

                # 조건에 모두 맞는 칵테일이 없는 경우
                if len(intersection) == 0:

                    for cocktail_id in result:
                        similar_cocktails = Cocktail.objects.filter(id=cocktail_id)
                        similar_serializer = RecommendSerializer(similar_cocktails, many=True)
                        similar_result.append(similar_serializer.data)

                    # 유사한 칵테일 반환
                    return Response({"similar cocktails": similar_result}, status=status.HTTP_200_OK)

            # 조건에 모두 맞는 칵테일이 있는 경우, 그 칵테일의 id를 유사한 칵테일 리스트에서 삭제
            for i in intersection:
                result.remove(i)
                fit_cocktails = Cocktail.objects.filter(id=i)
                fit_serializer = RecommendSerializer(fit_cocktails, many=True)
                fit_result.append(fit_serializer.data)

            for cocktail_id in result:
                similar_cocktails = Cocktail.objects.filter(id=cocktail_id)
                similar_serializer = RecommendSerializer(similar_cocktails, many=True)
                similar_result.append(similar_serializer.data)

            # 만족하는 교집합이 있다면 맞는 칵테일과 다른 추천 칵테일 정보 제공
            return Response({"fit cocktails": fit_result,
                             "similar cocktails": similar_result}, status=status.HTTP_200_OK)

        except:
            return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)
