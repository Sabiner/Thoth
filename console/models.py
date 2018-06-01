# coding=utf-8

from django.db import models
from common.decorator import get_none_if_no_value


class Article(models.Model):

    class Meta:
        db_table = 'article'

    type = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    create_time = models.DateTimeField()
    creator = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return self.type, self.title, self.create_time, self.creator

    @classmethod
    @get_none_if_no_value
    def get_all_info(cls):
        articles = cls.objects.all()
        return articles.values()
