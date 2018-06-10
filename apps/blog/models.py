# coding=utf-8

import os
from django.db import models
from console.common.decorator import get_none_if_no_value
from mdeditor.fields import MDTextField
from console.common.logger import getLogger
from console import config


log = getLogger()
conf = config.setup_config()


class Article(models.Model):

    class Meta:
        db_table = 'article'

    type = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    create_time = models.DateTimeField()
    creator = models.CharField(max_length=30)
    url = models.CharField(max_length=20)
    content = MDTextField()

    def __str__(self):
        return self.title.encode('utf-8')

    def save(self, *args, **kwargs):
        article_path = os.path.join(conf.get('article', 'path'), self.url)
        with open(article_path, 'w') as f:
            f.write(self.content)

        self.content = article_path
        super(Article, self).save(*args, **kwargs)

    def to_dict(self):
        content = self.content
        if os.path.exists(self.content):
            with open(self.content, 'r') as f:
                content = f.read()
        obj = {
            'type': self.type,
            'title': self.title,
            'create_time': self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            'creator': self.creator,
            'content': content,
            'url': self.url
        }
        return obj

    @classmethod
    @get_none_if_no_value
    def get_all_info(cls):
        articles = cls.objects.all()
        return articles.values()
