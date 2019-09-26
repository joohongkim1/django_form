from django.db import models


# 데이터베이스 모델링, 상속
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    # 메타 클래스
    class Meta:
        ordering = ('-pk',) # 마지막 생성 데이터가 가장 첫 번째로 오도록
                            # , 찍으면 튜플로 인식

    def __str__(self):
        return f'{self.pk} - {self.title}'
        