from rest_framework import serializers
from .models import Result


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['cocktail', 'mbti', 'cocktail_url', 'desc', 'fit_cocktail', 'fit_cocktail_url', 'unfit_cocktail',
                  'unfit_cocktail_url']
