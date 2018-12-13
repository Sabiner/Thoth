# coding=utf-8

import os
from django.contrib import admin
from models import Article
from console.common import logger

log = logger.getLogger()


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('type', 'title', 'creator', 'description', 'content')

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            if os.path.exists(obj.content):
                with open(obj.content, 'r') as f:
                    log.debug('open file')
                    obj.content = f.read()
        return super(ArticleAdmin, self).get_form(request, obj, **kwargs)
