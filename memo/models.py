from django.db import models
from django.contrib.auth.models import User # Userモデルをインポート
from django.urls import reverse

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=5,unique=True)

    def __str__(self):
        return self.name
    

class Memo(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField(max_length=50)
    tags = models.ManyToManyField(Tag, related_name='memos',blank=True)
    
    # その投稿の詳細ページへのリンク
    def get_absolute_url(self):
        return reverse("memo:detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title