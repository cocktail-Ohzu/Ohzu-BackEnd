from django.urls import path

from . import views

urlpatterns = [
    path('landingpage/result', views.ResultView.as_view()),  # 결과 페이지
]
