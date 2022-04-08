from django.db import models


# 기본 술
class Base(models.Model):
    name = models.CharField(max_length=20, unique=True)
    desc = models.CharField(max_length=50, blank=True, null=True)
    tag_color = models.CharField(max_length=10, blank=True, null=True)  # 태그 색상

    def __str__(self):
        return self.name


# 맛
class Flavor(models.Model):
    name = models.CharField(max_length=20, unique=True)
    tag_color = models.CharField(max_length=10, blank=True, null=True)  # 태그 색상
    group = models.PositiveIntegerField(default=0)  # 그룹

    def __str__(self):
        return self.name


# 무드
class Mood(models.Model):
    name = models.CharField(max_length=20, unique=True)
    tag_color = models.CharField(max_length=10, blank=True, null=True)  # 태그 색상
    group = models.PositiveIntegerField(default=0)  # 그룹

    def __str__(self):
        return self.name


# 가니쉬
class Ornament(models.Model):
    name = models.CharField(max_length=20, unique=True)
    tag_color = models.CharField(max_length=10, blank=True, null=True)  # 태그 색상

    def __str__(self):
        return self.name


# 재료
class Ingredient(models.Model):
    name = models.CharField(max_length=30, unique=True)
    desc = models.CharField(max_length=50, blank=True, null=True)
    tag_color = models.CharField(max_length=10, blank=True, null=True)  # 태그 색상

    def __str__(self):
        return self.name


# 날씨 & 계절
class Weather(models.Model):
    name = models.CharField(max_length=20, unique=True)
    tag_color = models.CharField(max_length=10, blank=True, null=True)  # 태그 색상

    def __str__(self):
        return self.name


# 메인 칵테일 모델
class Cocktail(models.Model):
    name = models.CharField(max_length=20, unique=True)
    eng_name = models.CharField(max_length=20)
    img = models.URLField()
    background_color = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)  # 한줄 소개
    strength = models.IntegerField()
    cocktail_color = models.CharField(max_length=10)
    recipe = models.TextField()
    ohzu_point = models.TextField(blank=True)
    # many to many 필드들
    bases = models.ManyToManyField(Base, through='Cocktail_Base')  # 기본 술
    flavors = models.ManyToManyField(Flavor, through='Cocktail_Flavor')  # 맛
    moods = models.ManyToManyField(Mood, through='Cocktail_Mood')  # 무드
    ornaments = models.ManyToManyField(Ornament, through='Cocktail_Ornament')  # 가니쉬
    ingredients = models.ManyToManyField(Ingredient, through='Cocktail_Ingredient')  # 재료
    weathers = models.ManyToManyField(Weather, through='Cocktail_Weather')  # 날씨 & 계절

    def __str__(self):
        return self.name

    def get_bases(self):
        return ", ".join([p.name for p in self.bases.all()])

    def get_flavors(self):
        return ", ".join([p.name for p in self.flavors.all()])

    def get_moods(self):
        return ", ".join([p.name for p in self.moods.all()])

    def get_ornaments(self):
        return ", ".join([p.name for p in self.ornaments.all()])

    def get_ingredients(self):
        return ", ".join([p.name for p in self.ingredients.all()])

    def get_weathers(self):
        return ", ".join([p.name for p in self.weathers.all()])


# 중개 모델 #

#  칵테일 - 재료 중개 모델
class Cocktail_Ingredient(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)  # 해당 칵테일
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)  # 해당 재료
    amount = models.CharField(max_length=20)  # 해당 칵테일 재료의 양

    def get_ingredient(self):
        return self.ingredient.name

    def get_cocktail(self):
        return self.cocktail.name


#  칵테일 - 기본 술 중개 모델
class Cocktail_Base(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)  # 해당 칵테일
    base = models.ForeignKey(Base, on_delete=models.CASCADE)  # 해당 재료

    def get_base(self):
        return self.base.name

    def get_cocktail(self):
        return self.cocktail.name


#  칵테일 - 맛 중개 모델
class Cocktail_Flavor(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)

    def get_flavor(self):
        return self.flavor.name

    def get_cocktail(self):
        return self.cocktail.name


#  칵테일 - 무드 중개 모델
class Cocktail_Mood(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)

    def get_mood(self):
        return self.mood.name

    def get_cocktail(self):
        return self.cocktail.name


#  칵테일 - 장식 중개 모델
class Cocktail_Ornament(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    ornament = models.ForeignKey(Ornament, on_delete=models.CASCADE)

    def get_ornament(self):
        return self.ornament.name

    def get_cocktail(self):
        return self.cocktail.name


#  칵테일 - 날씨 중개 모델
class Cocktail_Weather(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    weather = models.ForeignKey(Weather, on_delete=models.CASCADE)

    def get_weather(self):
        return self.weather.name

    def get_cocktail(self):
        return self.cocktail.name