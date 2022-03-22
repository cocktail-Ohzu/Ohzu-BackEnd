from django.db import models
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase


class BaseTag(TagBase):
    class Meta:
        verbose_name = _("BaseTag")
        verbose_name_plural = _("BaseTags")


class ThroughBaseTag(GenericTaggedItemBase):
    tag = models.ForeignKey(
        BaseTag,
        on_delete=models.CASCADE,
    )


class FlavorTag(TagBase):
    class Meta:
        verbose_name = _("FlavorTag")
        verbose_name_plural = _("FlavorTags")


class ThroughFlavorTag(GenericTaggedItemBase):
    tag = models.ForeignKey(
        FlavorTag,
        on_delete=models.CASCADE,
    )


class MoodTag(TagBase):
    class Meta:
        verbose_name = _("MoodTag")
        verbose_name_plural = _("MoodTags")


class ThroughMoodTag(GenericTaggedItemBase):
    tag = models.ForeignKey(
        MoodTag,
        on_delete=models.CASCADE,
    )


class OrnamentTag(TagBase):
    class Meta:
        verbose_name = _("OrnamentTag")
        verbose_name_plural = _("OrnamentTags")


class ThroughOrnamentTag(GenericTaggedItemBase):
    tag = models.ForeignKey(
        OrnamentTag,
        on_delete=models.CASCADE,
    )


class WeatherSeasonTag(TagBase):
    class Meta:
        verbose_name = _("WeatherSeasonTag")
        verbose_name_plural = _("WeatherSeasonTags")


class ThroughWeatherSeasonTag(GenericTaggedItemBase):
    tag = models.ForeignKey(
        WeatherSeasonTag,
        on_delete=models.CASCADE,
    )


class IngredientsRecTag(TagBase):
    class Meta:
        verbose_name = _("IngredientsRecTag")
        verbose_name_plural = _("IngredientsRecTags")


class ThroughIngredientsRecTag(GenericTaggedItemBase):
    tag = models.ForeignKey(
        IngredientsRecTag,
        on_delete=models.CASCADE,
    )


class Cocktail(models.Model):
    name = models.CharField(max_length=20)
    eng_name = models.CharField(max_length=20)
    img = models.URLField()
    desc = models.CharField(max_length=50)  # 한줄 소개
    strength = models.IntegerField()
    color = models.CharField(max_length=10)
    recipe = models.TextField()
    ohzu_point = models.TextField()
    base = TaggableManager(through=ThroughBaseTag)
    flavor = TaggableManager(through=ThroughFlavorTag)
    mood = TaggableManager(through=ThroughMoodTag)
    ornament = TaggableManager(through=ThroughOrnamentTag)  # 가니쉬
    weather_and_season = TaggableManager(through=ThroughWeatherSeasonTag)
    ingredients_rec = TaggableManager(blank=True, through=ThroughIngredientsRecTag)  # 다른 재료 추천


class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)


# 중개 모델
class Cocktail_Ingredient(models.Model):
    amount = models.CharField(max_length=20)

    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
