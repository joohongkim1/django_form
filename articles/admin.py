from django.contrib import admin
from .models import Article # 같은 어플 내에 있는 models 에서 Article 을 불러오겠다.


@admin.register(Article)
# 상속
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'create_at', 'updated_at',)