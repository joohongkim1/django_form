from django.urls import path
from . import views  # 같은 어플리케이션 내에서 view 함수를 꺼내겠다.

app_name = 'articles'

# www.domain.com/articles/ ____
urlpatterns = [
    path('', views.index, name='index'),  # articles:index 로 접근 (다른 앱에도 index 페이지가 있을 수 있어서)
    path('create/', views.create, name='create'), # view 함수 매핑
    path('<int:article_pk>/', views.detail, name='detail'),
]
