# coding=utf-8

from django.db import models
from console.common.decorator import get_none_if_no_value
from django_markdown.models import MarkdownField


class Article(models.Model):

    class Meta:
        db_table = 'article'

    type = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    create_time = models.DateTimeField()
    creator = models.CharField(max_length=30)
    url = models.CharField(max_length=20)
    content = MarkdownField()

    def __str__(self):
        obj = {
            'type': self.type,
            'title': self.title,
            'create_time': self.create_time,
            'creator': self.creator,
            'content': self.content,
            'url': self.url
        }
        return obj

    @classmethod
    @get_none_if_no_value
    def get_all_info(cls):
        articles = cls.objects.all()
        return articles.values()
