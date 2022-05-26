from django.urls import path

from . import views

urlpatterns = [
    path('main', views.MainCocktailView.as_view()),  # 메인 페이지
    path('cocktails/<int:id>', views.DetailCocktailView.as_view()),  # 상세 페이지
    path('search', views.SearchTagView.as_view()),  # 검색 api
    path('recommend', views.RecommendView.as_view()),  # 추천 페이지
]