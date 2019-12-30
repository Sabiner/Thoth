# -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework import viewsets
from article.models import Article


class ArticleView(viewsets.ViewSet):

    def show_latest_article(self, request):
        """
        展示最新的 10 条记录
        """
        try:
            all_article = Article.objects.all().order_by('-create_at')[0: 6]
            information = [article.to_dict() for article in all_article]
        except Exception as e:
            raise e

        response = dict(articles=information)
        return render(request, 'article/blog.html', response)
