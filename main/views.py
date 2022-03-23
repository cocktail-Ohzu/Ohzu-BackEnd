from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from .models import Cocktail
from .serializers import MainSerializer


class MainCocktailView(APIView):
    def get(self, request):
        today = datetime.today()
        today_cocktail = (today.year + today.month + today.day) % 36  # 오늘의 추천 칵테일 랜덤
        cocktail = get_object_or_404(Cocktail, id=today_cocktail+1)
        serializer = MainSerializer(cocktail)
        return Response(serializer.data)
