# coding=utf-8

from models import Article


class ArticleService(object):
    """
    Article service.
    Any operation about article deal with in there.
    """
    def __init__(self):
        pass

    @classmethod
    def create(cls, _type, title, create_time, creator, content):
        try:
            args = (_type, title, create_time, creator, content)
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
                content=content
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
