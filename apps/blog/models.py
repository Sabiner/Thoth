# coding=utf-8

import os
from django.db import models
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
    create_time = models.DateTimeField(auto_now_add=True)
    creator = models.CharField(max_length=30)
    description = models.TextField(max_length=400)
    content = MDTextField()

    list_display = ('type', 'title', 'create_time', 'creator', 'description')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        article_path = os.path.join(conf.get('article', 'path'), self.create_time.strftime("%Y%m%d%H%M%S"))
        with open(article_path, 'w') as f:
            f.write(self.content.encode('utf-8'))

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
        }
        return obj
