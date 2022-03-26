from django.db import models


# 기본 술
class Base(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# 맛
class Flavor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# 무드
class Mood(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# 가니쉬
class Ornament(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# 재료
class Ingredient(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# 날씨 & 계절
class Weather(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# 메인 칵테일 모델
class Cocktail(models.Model):
    name = models.CharField(max_length=20)
    eng_name = models.CharField(max_length=20)
    img = models.URLField()
    background_color = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)  # 한줄 소개
    strength = models.IntegerField()
    cocktail_color = models.CharField(max_length=10)
    recipe = models.TextField()
    ohzu_point = models.TextField()
    # many to many 필드들
    bases = models.ManyToManyField(Base, through='Cocktail_Base')  # 기본 술
    flavors = models.ManyToManyField(Flavor)  # 맛
    moods = models.ManyToManyField(Mood)  # 무드
    ornaments = models.ManyToManyField(Ornament)  # 가니쉬
    ingredients = models.ManyToManyField(Ingredient, through='Cocktail_Ingredient')  # 재료
    weathers = models.ManyToManyField(Weather)  # 날씨 & 계절

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


#  칵테일 - 재료 중개모델
class Cocktail_Ingredient(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)  # 해당 칵테일
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)  # 해당 재료
    amount = models.CharField(max_length=20)  # 해당 칵테일 재료의 양


#  칵테일 - 기본 술 중개모델
class Cocktail_Base(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)  # 해당 칵테일
    base = models.ForeignKey(Base, on_delete=models.CASCADE)  # 해당 재료
    amount = models.CharField(max_length=20)  # 해당 칵테일 재료의 양
