from django.urls import path
from . import views

urlpatterns = [
    path('arts/', views.articles, name='articles'),
    path('artdetails/', views.article_detail, name='article_detail'),
]