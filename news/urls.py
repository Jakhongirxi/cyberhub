from django.urls import path

from news import views


app_name = 'news'

urlpatterns = [
    path('', views.news_view, name='index'),
    path('news/detail/<int:pk>/', views.news_detail, name='news_detail')
]