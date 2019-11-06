# coding=utf-8

import os
import uuid
from datetime import datetime

from django.db import models
from mdeditor.fields import MDTextField
from console.common.logger import getLogger
from console import config


log = getLogger()
conf = config.setup_config()


class Article(models.Model):

    id = models.CharField(unique=True, max_length=40, primary_key=True, default=uuid.uuid4())
    title = models.CharField(max_length=200, null=True, blank=True)
    creator = models.CharField(max_length=50)
    create_at = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    tag = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=400)
    content_path = models.CharField(max_length=255, null=True, blank=True)

    list_display = ('title', 'type', 'tag', 'create_at', 'creator', 'description')

    class Meta:
        managed = False
        db_table = 'article'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)
        article_path = os.path.join(conf.get('article', 'path'), str(self.id))
        with open(article_path, 'w') as f:
            f.write(self.content.encode('utf-8'))

        self.content = article_path
        super(Article, self).save(*args, **kwargs)
    
    def to_dict(self):
        content = self.content
        if os.path.exists(self.content):
            with open(self.content, 'r') as f:
                content = f.read()
        return dict(
            title=self.title,
            type=self.type,
            tag=self.tag,
            create_at=self.create_at,
            creator=self.creator,
            content=content,
        )
