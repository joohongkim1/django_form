from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

# 모든 article 을 보여주는 페이지
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)  # article 의 index 페이지를 보여주겠다.


# GET 으로 들어오면 생성하는 페이지 rendering
# POST 로 들어오면 생성하는 로직 수행
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article(title=title, content=content)
            article.save()
            return redirect('articles:index')  # redirect 는 django.shortcuts 에서 import
        # else:
        #     context = {'form': form}
        #     return render(request, 'articles/create.html', context)
    else:  # GET 요청일 경우
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/create.html', context)

def detail(request, article_pk): # 데이터 하나 꺼내는 페이지
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article}
    return render(request, 'articles/detail.html', context)
