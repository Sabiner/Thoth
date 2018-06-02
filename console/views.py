# coding=utf-8
"""
Index view
"""
from django.views.generic import View
from django.shortcuts import render_to_response
from apps.blog.service import ArticleService


class Index(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('index/index.html')


class Tags(View):
    def get(self, request, *args, **kwargs):
        return render_to_response('tags/tags.html')


class Blog(View):
    def get(self, request, *args, **kwargs):
        articles = ArticleService.get()
        params = {
            'articles': articles
        }
        return render_to_response('blog/blog.html', params)
