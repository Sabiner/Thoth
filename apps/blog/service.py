# coding=utf-8

import os
import copy
from datetime import datetime

from console import config
from models import Article
from console.common.logger import getLogger

log = getLogger()
conf = config.setup_config()


class ArticleService(object):
    """
    Article service.
    Any operation about article deal with in there.
    """
    def __init__(self):
        pass

    @classmethod
    def create(cls, _type, title, creator, content):
        log.debug(_type, title, creator, content)
        if not all((_type, title, creator, content)):
            return False
        else:
            article = Article(
                type=_type,
                title=title,
                creator=creator,
                content=content
            )

            article.save()
            return True

    @classmethod
    def get(cls):
        information = {
            'news': list()
        }
        try:
            all_type = Article.objects.values('type').distinct()
            for _type in all_type:
                t = _type.get('type')
                articles_a_type = Article.objects.filter(type=t).order_by('-create_at')[0: 10]
                information[t] = articles_a_type

            all_article = Article.objects.all().order_by('-create_at')[0: 10]
            for article in all_article:
                content_path = copy.copy(article.content)
                if os.path.exists(content_path):
                    with open(content_path, 'r') as f:
                        article.content = f.read()

                information['news'].append(article)
        except Exception, e:
            log.debug(e)
        return information

    @classmethod
    def get_blog_by_url(cls, url):
        """
        Get blog details information by url.
        :param url: article url.
        :return: blog detail
        """
        if not url:
            return dict()
        url_path = os.path.join(conf.get('article', 'path'), url)
        blog = Article.objects.get(content=url_path)
        blog = blog.to_dict()

        return blog

    @classmethod
    def get_blog_by_type(cls, _type, start, end):
        """
        Filter blog information by article type.
        :param _type: article type.
        :param start: limit start
        :param end: limit end.
        :return: articles
        """
        try:
            assert isinstance(start, int)
            assert isinstance(end, int)
        except AssertionError, e:
            log.debug(e)
            return False

        articles = Article.objects.filter(type=_type).order_by('-create_at')[start: end]
        return articles
