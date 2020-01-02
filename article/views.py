# -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework import viewsets
from article.service import ArticleService


class ArticleView(viewsets.ViewSet):

    @classmethod
    def get_latest_article(cls, request):
        """
        展示最新的 6 条记录
        """
        response = dict(articles=ArticleService().get_latest_articles())
        return render(request, 'article/blog.html', response)

    @classmethod
    def get_ranking_list(cls, request):
        """
        展示首页排行榜
        """
        response = dict(
            traffic_list=ArticleService().get_traffic_list(),
            latest_list=ArticleService().get_latest_articles(),
            recommended_list=ArticleService().get_recommended_list()
        )
        return render(request, 'index/ranking_list.html', response)

    @classmethod
    def get_by_id(cls, request, article_id):
        article = ArticleService().get_by_id(article_id)
        return render(request, 'article/article_content.html', dict(article=article))

    @classmethod
    def get_correlation(cls, request):
        response = dict(
            correlations=ArticleService().get_correlation_list()
        )
        return render(request, 'article/correlation.html', response)
