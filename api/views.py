from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from articles.models import Article
from django.core import serializers
from django.http import HttpResponse

def articles(request):
    articles = Article.objects.all().order_by('date')
    article_list = serializers.serialize('json', articles)
    return HttpResponse(article_list, content_type="text/json-comment-filtered")

def article_detail(request, slug):
  detailed_article = Article.objects.get(slug=slug)
  article_detail = serializers.serialize('json', detailed_article)
  return HttpResponse(article_detail, content_type="text/json-comment-filtered")
