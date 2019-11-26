from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import Article
from . import forms

# Create your views here.

class SearchResultsView(ListView):
    model = Article
    template_name = 'articles/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Article.objects.filter(
            Q(title__icontains = query) 
        )
        return object_list

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html', {'articles':articles})

def article_detail(request, slug):
    #return HttpResponse(slug)
    # article = Article.objects.get(slug=slug)
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})

@login_required(login_url = "/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})

def article_aboutme(request):
    return render(request, "articles/aboutme.html")