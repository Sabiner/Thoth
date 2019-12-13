# coding: utf-8

import os
from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'type', 'tag', 'creator')  # 列表展示
    search_fields = ('title', 'tag')    # 搜索
    list_filter = ('type', 'tag')       # 过滤
    list_editable = ('type', 'tag')     # 可编辑

    def get_fieldsets(self, request, obj=None):
        if obj and os.path.exists(obj.content_path):
            with open(obj.content_path, 'r') as f:
                obj.content_path = f.read()
        return super(ArticleAdmin, self).get_fieldsets(request, obj)
