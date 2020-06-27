from django.urls import re_path
from django.conf.urls import url
from . import views
app_name='articles'
urlpatterns = [
  url(r'^$', views.article_list,name="list"),
  re_path('create/', views.article_create, name="create"),
  url(r'^(?P<slug>[\w-]+)/$', views.article_detail,name="detail")
]