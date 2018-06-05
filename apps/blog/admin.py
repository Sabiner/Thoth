# coding=utf-8

from django.contrib import admin
from models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('type', 'title', 'create_time', 'creator', 'url', 'content')
