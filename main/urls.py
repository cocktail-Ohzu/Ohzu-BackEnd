from django.urls import path

from . import views

urlpatterns = [
    path('main', views.MainCocktailView.as_view()), # 메인 페이지
    path('cocktails/<int:id>', views.DetailCocktailView.as_view()), # 상세 페이지
]
