from django.db import models


# 질문
class Question(models.Model):
    title = models.TextField()
    attribute = models.CharField(max_length=5)  # 왼쪽이 '예'를 선택할 경우의 속성이 되도록 저장 (ex. NS, IE)

    def __str__(self):
        return self.title


# 결과
class Result(models.Model):
    cocktail = models.CharField(max_length=20)  # 해당 칵테일 이름
    mbti = models.CharField(max_length=5)  # 해당 칵테일 mbti (ex. EST, ENF ...)
    cocktail_img = models.URLField()  # 칵테일 이미지
    desc = models.TextField()  # 칵테일 설명
    fit_cocktail = models.CharField(max_length=20)  # 잘 맞는 칵테일 이름
    fit_cocktail_url = models.URLField()  # 잘 맞는 칵테일 이미지 url
    unfit_cocktail = models.CharField(max_length=20)  # 안 맞는 칵테일 이름
    unfit_cocktail_url = models.URLField()  # 안 맞는 칵테일 이미지 url
