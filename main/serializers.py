from rest_framework import serializers
from .models import Cocktail


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = ['id', 'img', 'name', 'eng_name', 'desc', 'strength']
