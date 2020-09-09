from django.urls import path, include
from exam import views

urlpatterns = [
    path('', views.ConfigView.as_view(), name='config'),
    path('exam/', views.ExamView.as_view(), name='exam'),
    path('result/', views.ResultView.as_view(), name='result'),
    path('report/', views.ReportView.as_view(), name='report'),
]
