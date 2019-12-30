# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import ArticleView

urlpatterns = [
    url(r'show_latest_article?$', ArticleView.as_view({'get': 'show_latest_article'}), name='show_latest_article'),
]