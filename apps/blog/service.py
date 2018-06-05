# coding=utf-8

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
        articles = Article.get_all_info()
        blog_information = dict()
        for article in articles:
            _type = article.get('type')

            if _type not in blog_information:
                blog_information[_type] = [article]
            else:
                blog_information[_type].append(article)

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
