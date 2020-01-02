from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CreateArticle, EditArticle
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Q
from .models import Article

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
    # Pagination
    paginator = Paginator(articles, 3) # Show 3 contacts per page
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    
    return render(request,'articles/article_list.html', {'articles':articles})

def article_detail(request, slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    # article = get_object_or_404(Article, id=id)
    return render(request, 'articles/article_detail.html', {'article':article})

@login_required(login_url = "/accounts/login/")
def article_create(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    if request.method == 'POST':
        form = CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            #save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, ('created successfully:)'), extra_tags='alert alert-success')
            # return redirect('articles:list')
            return HttpResponseRedirect(instance.get_absolute_url())
    else:
        form = CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})

def edit(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    article = get_object_or_404(Article, slug=slug)
    form = EditArticle(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        form.save()
        messages.success(request, ('item edit successfully!'), extra_tags='alert alert-success')
        return HttpResponseRedirect(article.get_absolute_url())
        # return redirect('articles:detail', id=id)
    return render(request, 'articles/edit.html', {'form':form})

def delete(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    # article = Article.objects.get(id = id)
    article = get_object_or_404(Article, slug=slug)
    if article.delete():
        messages.success(request, ('item deleted successfully!'), extra_tags='alert alert-success')
        return redirect('articles:list')
    # return render(request,'articles/article_list.html', {'article':article})

def article_aboutme(request):
    return render(request, "articles/aboutme.html")