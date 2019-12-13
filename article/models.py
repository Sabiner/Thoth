# coding: utf-8

import os
import uuid
from django.db import models
from mdeditor.fields import MDTextField

from Thoth.utils import Config

conf = Config()


class Article(models.Model):

    id = models.CharField(unique=True, max_length=40, primary_key=True, default=uuid.uuid4())
    title = models.CharField(max_length=200, null=True, blank=True)
    creator = models.CharField(max_length=50)
    create_at = models.DateField(auto_now_add=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    tag = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=400)
    content_path = MDTextField()

    list_display = ('title', 'type', 'tag', 'create_at', 'creator', 'description')

    class Meta:
        managed = False
        db_table = 'article'

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        article_path = os.path.join(conf.article_path, str(self.id))
        with open(article_path, 'w') as f:
            f.write(self.content_path)
        self.content_path = article_path
        super(Article, self).save(force_insert, force_update, using, update_fields)
