from django.db import models
from django.utils import timezone

class Day(models.Model):
    title=models.CharField("タイトル",max_length=200)
    text=models.TextField("本文",default="本文を入力してください")
    date=models.DateTimeField("日付",default=timezone.now)
# Create your models here.
    def __str__(self):
        return self.title