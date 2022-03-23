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
    base = TaggableManager(through=ThroughBaseTag, help_text='List all the available base tags here.')
    flavor = TaggableManager(through=ThroughFlavorTag, help_text='List all the available flavor tags here.')
    mood = TaggableManager(through=ThroughMoodTag, help_text='List all the available mood tags here.')
    ornament = TaggableManager(blank=True, through=ThroughOrnamentTag, help_text='List all the available ornament tags here.')
    weather_and_season = TaggableManager(through=ThroughWeatherSeasonTag, help_text='List all the available weather and season tags here.')
    ingredients_rec = TaggableManager(blank=True, through=ThroughIngredientsRecTag, help_text='List all the available ingredients_rec tags here.')  # 다른 재료 추천

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


# 중개 모델
class Cocktail_Ingredient(models.Model):
    amount = models.CharField(max_length=20)

    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
