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
    def create(cls, _type, title, create_time, creator, content):
        if not all((_type, title, create_time, creator, content)):
            return False
        else:
            article = Article(
                type=_type,
                title=title,
                create_time=create_time.strftime("%Y-%m-%d %H:%M:%S"),
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
                articles_a_type = Article.objects.filter(type=t).order_by('-create_time')[0: 10]
                for article in articles_a_type:
                    article.url = cls.date_to_string(article.create_time)
                information[t] = articles_a_type

            all_article = Article.objects.all().order_by('-create_time')[0: 10]
            for article in all_article:
                article.url = cls.date_to_string(article.create_time)
                article.create_time = article.create_time.strftime("%Y-%m-%d %H:%M:%S")

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
        create_time = cls.string_to_date(url)
        blog = Article.objects.get(create_time=create_time)
        log.debug(blog)
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

        articles = Article.objects.filter(type=_type).order_by('-create_time')[start: end]
        for article in articles:
            article.create_time = article.create_time.strftime("%Y-%m-%d %H:%M:%S")

        return articles

    @staticmethod
    def date_to_string(date):
        return date.strftime("%Y%m%d%H%M%S")

    @staticmethod
    def string_to_date(_str):
        return '%s-%s-%s %s:%s:%s' % (_str[:4], _str[4:6], _str[6:8], _str[8:10], _str[10: 12], _str[12:])
