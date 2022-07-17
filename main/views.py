import random

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from .models import Cocktail, Cocktail_Base, Cocktail_Ingredient, Cocktail_Flavor, Cocktail_Mood, Cocktail_Weather, \
    Cocktail_Ornament, Flavor, Mood, Base, Ingredient, Weather, Ornament
from .serializers import MainSerializer, DetailSerializer, BaseSerializer, IngredientSerializer, SearchSerializer, \
    RecommendSerializer, RecommendBaseSerializer, RecommendIngredientSerializer, RecommendMoodSerializer, \
    RecommendOrnamentSerializer, RecommendWeatherSerializer, RecommendFlavorSerializer

# 도수 기준 (standard_strength[index] = [시작 도수, 끝 도수])
standard_strength = [[0, 0], [1, 10], [12, 20], [32, 40]]


# 도수 번호(1~4)가 들어왔을 때, 그에 맞는 시작, 끝 도수 반환
def strength_range(strength):
    return standard_strength[strength - 1]


# GET /recommend의 재료 필드 카테고리화 함수
def ingredient_result(category, category_list):
    for ingredient_id in category:
        ingredients = Ingredient.objects.get(id=ingredient_id)
        ingredient_serializer = RecommendIngredientSerializer(ingredients)
        category_list.append(ingredient_serializer.data)

    return category_list


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
    # 추천 필드 제공 api
    def get(self, request):
        try:
            # ingredients_id = [2, 3, 9, 11, 18, 22, 24, 27, 28, 29, 31, 32, 35, 36, 38, 40]
            essence_or_alcohol = [24, 28, 29, 32, 35]
            juice = [11, 18, 27, 30, 31]
            soft_drink = [2, 22, 38, 40]
            etc = [3, 9]

            essence_or_alcohol_list = []
            juice_list = []
            soft_drink_list = []
            etc_list = []

            bases_serializer = RecommendBaseSerializer(Base.objects.all(), many=True)
            flavors_serializer = RecommendFlavorSerializer(Flavor.objects.all(), many=True)
            moods_serializer = RecommendMoodSerializer(Mood.objects.all(), many=True)
            weathers_serializer = RecommendWeatherSerializer(Weather.objects.all(), many=True)
            ornaments_serializer = RecommendOrnamentSerializer(Ornament.objects.all(), many=True)

            return Response({"bases": bases_serializer.data,
                             "ingredients":
                                 {
                                     "essence_or_alcohol": ingredient_result(essence_or_alcohol, essence_or_alcohol_list),
                                     "juice": ingredient_result(juice, juice_list),
                                     "soft_drink": ingredient_result(soft_drink, soft_drink_list),
                                     "etc": ingredient_result(etc, etc_list)
                                 },
                             "flavors": flavors_serializer.data,
                             "moods": moods_serializer.data,
                             "weathers": weathers_serializer.data,
                             "ornaments": ornaments_serializer.data})

        except:
            return Response({"message": "error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            # 딱 맞는 결과가 없을 경우, 빈도가 가장 많은, 유사한 칵테일을 추천하기 위한 리스트
            result_cocktail = []
            # 알맞는 칵테일을 추천하기 위한 리스트
            data = []

            # 유저가 추천 받고자 하는 필드 저장
            id_list = list(request.data)

            # 요청이 없는 경우, random으로 칵테일 추천
            if len(id_list) == 0:
                random_ids = []
                recommend_result = []

                while len(random_ids) < 4:
                    random_id = random.randrange(1, 36)
                    if random_id in random_ids:
                        continue
                    else:
                        random_ids.append(random_id)

                for cocktail_id in random_ids:
                    recommend_cocktails = Cocktail.objects.get(id=cocktail_id)
                    recommend_serializer = RecommendSerializer(recommend_cocktails)
                    recommend_result.append(recommend_serializer.data)

                return Response({"recommend_cocktails": recommend_result}, status=status.HTTP_303_SEE_OTHER)

            else:
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

                        # 검색한 맛, 그 맛과 유사한 태그의 group 값을 저장하는 리스트
                        similar_flavor_group = []

                        # 유사한 태그의 id 저장 리스트
                        similar_flavor_id = []

                        for i in request.data['flavor_id']:
                            selected_flavor = Flavor.objects.get(id=i)
                            similar_flavor_group.append(selected_flavor.group)

                        similar_flavor_group = list(set(similar_flavor_group))

                        for group in similar_flavor_group:
                            similar_flavors = Flavor.objects.filter(group=group)

                            for similar_flavor in similar_flavors:
                                similar_flavor_id.append(similar_flavor.id)

                        for i in similar_flavor_id:
                            flavors = Cocktail_Flavor.objects.filter(flavor_id=i)

                            for flavor in flavors:
                                result_cocktail.append(flavor.cocktail_id)
                                flavor_cocktail.append(flavor.cocktail_id)

                        data.append(flavor_cocktail)
                        continue

                    # 무드/기분 추천
                    if tag_id == 'mood_id':
                        mood_cocktail = []

                        # 검색한 무드/기분, 그 무드/기분과 유사한 태그의 group 값을 저장하는 리스트
                        similar_mood_group = []

                        # 유사한 태그의 id 저장 리스트
                        similar_mood_id = []

                        for i in request.data['mood_id']:
                            selected_mood = Mood.objects.get(id=i)
                            similar_mood_group.append(selected_mood.group)

                        similar_mood_group = list(set(similar_mood_group))

                        for group in similar_mood_group:
                            similar_moods = Mood.objects.filter(group=group)

                            for similar_mood in similar_moods:
                                similar_mood_id.append(similar_mood.id)

                        for i in similar_mood_id:
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
                    if tag_id == 'strength':
                        strength_cocktail = []

                        for i in request.data['strength']:
                            cocktails = Cocktail.objects.filter(strength__range=strength_range(i))

                            for cocktail in cocktails:
                                result_cocktail.append(cocktail.id)
                                strength_cocktail.append(cocktail.id)

                        data.append(strength_cocktail)
                        continue

                # 유사한 칵테일 id 리스트
                similar_result = []

                # 조건을 모두 만족 시키는 칵테일 id 리스트
                fit_result = []

                # 사용자가 선택한 필드들에 맞는 칵테일 빈도수 높은 순으로 정렬
                result = []
                result_cocktail = sorted(result_cocktail, key=lambda x: result_cocktail.count(x), reverse=True)
                for v in result_cocktail:
                    if v not in result:
                        result.append(v)

                # 사용자가 선택한 필드들을 모두 만족하는 칵테일 얻기 위한 교집합 intersection 변수
                intersection = list(set(data[0]))

                # data에 담긴 리스트들을 돌면서 교집합 확인
                for i in range(1, len(data)):
                    intersection = list((set(intersection) & set(data[i])))

                    # 조건에 모두 맞는 칵테일이 없는 경우
                    if len(intersection) == 0:

                        for cocktail_id in result:
                            similar_cocktails = Cocktail.objects.get(id=cocktail_id)
                            similar_serializer = RecommendSerializer(similar_cocktails)
                            similar_result.append(similar_serializer.data)

                        # 유사한 칵테일 반환
                        return Response({"similar_cocktails": similar_result}, status=status.HTTP_200_OK)

                # 조건에 모두 맞는 칵테일이 있는 경우, 그 칵테일의 id를 유사한 칵테일 리스트에서 삭제
                for i in intersection:
                    result.remove(i)
                    fit_cocktails = Cocktail.objects.get(id=i)
                    fit_serializer = RecommendSerializer(fit_cocktails)
                    fit_result.append(fit_serializer.data)

                for cocktail_id in result:
                    similar_cocktails = Cocktail.objects.get(id=cocktail_id)
                    similar_serializer = RecommendSerializer(similar_cocktails)
                    similar_result.append(similar_serializer.data)

                # 만족하는 교집합이 있다면 맞는 칵테일과 다른 추천 칵테일 정보 제공
                return Response({"fit_cocktails": fit_result,
                                 "similar_cocktails": similar_result}, status=status.HTTP_200_OK)

        except:
            return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)
