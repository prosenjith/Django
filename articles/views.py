from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import forms

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
  detailed_article = Article.objects.get(slug=slug)
  return render(request, 'articles/article_detail.html', {'article2': detailed_article})

@login_required(login_url="/accounts/login/")
def article_create(request):
  if request.method == 'POST':
    article_form = forms.CreateArticle(request.POST, request.FILES)
    if article_form.is_valid():
      instance = article_form.save(commit=False)
      instance.author = request.user
      instance.save()
      return redirect('articles:list')
  else:
    article_form = forms.CreateArticle()
  return render(request, 'articles/article_create.html', {'articleForm': article_form})