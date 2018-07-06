# coding=utf-8
"""
Index view
"""
from django.views.generic import View
from django.shortcuts import render
from django.template.loader import render_to_string

from apps.blog.service import ArticleService


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index/index.html')


class Tags(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tags/tags.html')


class Blog(View):
    def get(self, request, *args, **kwargs):
        articles = ArticleService.get()
        params = {
            'articles': articles
        }
        return render(request, 'blog/blog.html', params)
