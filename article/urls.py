# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import ArticleView

urlpatterns = [
    url(r'^(?P<article_id>[a-z0-9-]+)?$', ArticleView.as_view({'get': 'get_by_id'}), name='get_by_id'),
    url(r'get_latest_article?$', ArticleView.as_view({'get': 'get_latest_article'}), name='get_latest_article'),
    url(r'get_ranking_list?$', ArticleView.as_view({'get': 'get_ranking_list'}), name='get_ranking_list'),
    url(r'get_correlation?$', ArticleView.as_view({'get': 'get_correlation'}), name='get_correlation'),
]
