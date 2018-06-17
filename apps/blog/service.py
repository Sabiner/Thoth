# coding=utf-8

import os
import copy
from models import Article
from console.common.logger import getLogger

log = getLogger()


class ArticleService(object):
    """
    Article service.
    Any operation about article deal with in there.
    """
    def __init__(self):
        pass

    @classmethod
    def create(cls, _type, title, create_time, creator, content, url):
        try:
            args = (_type, title, create_time, creator, content, url)
            for arg in args:
                assert arg is not None
        except AssertionError, e:
            return False
        else:
            article = Article(
                type=_type,
                title=title,
                create_time=create_time,
                creator=creator,
                content=content,
                url=url
            )
            article.save()
            return True

    @classmethod
    def get(cls):
        all_types = list()
        blog_information = {'news': list()}

        articles = Article.objects.all().order_by('-create_time')[0: 10]
        all_type = Article.objects.values('type').distinct()
        for _type in all_type:
            all_types.append(_type.get('type'))

        for _type in all_types:
            belongs_articles = Article.objects.filter(type=_type).order_by('-create_time')[0: 10]
            blog_information[_type] = belongs_articles

        for article in articles:
            article.create_time = article.create_time.strftime("%Y-%m-%d %H:%M:%S")

            content_path = copy.copy(article.content)
            if os.path.exists(content_path):
                with open(content_path, 'r') as f:
                    article.content = f.read()

            blog_information['news'].append(article)

        return blog_information

    @classmethod
    def get_blog_by_url(cls, url):
        try:
            assert url is not None
        except AssertionError, e:
            return False

        blog = Article.objects.get(url=url)
        blog = blog.to_dict()

        return blog
