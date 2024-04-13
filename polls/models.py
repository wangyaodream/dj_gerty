import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        # 在获取数据库内容比如q.objects.all()，所展示出来的内容
        return self.question_text

    @admin.display(
        boolean=True,  # 以图标的形式显示
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Info(models.Model):
    site_url = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    remark = models.CharField(max_length=200)
