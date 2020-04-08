# coding: utf-8

import os
import markdown
from article.models import Article

from Thoth.utils import load_logger

logger = load_logger()


class ArticleService(object):

    def get_latest_articles(self):
        """
        获取最新的博客
        :return: 最新博文集合
        """
        top_list = Article.objects.all().order_by('-create_at')[0: 6]
        return [i.to_dict() for i in top_list]

    def get_traffic_list(self):
        """
        获取访问量排行榜前 6 位
        :return: 博文集合
        """
        top_list = Article.objects.all().order_by('-pv_count', )[0: 6]
        return [i.to_dict() for i in top_list]

    def get_recommended_list(self):
        """
        获取站长推荐排行榜前 6 位
        :return: 博文集合
        """
        # TODO: 完成推荐部分
        top_list = Article.objects.all().order_by('create_at')[0: 6]
        return [i.to_dict() for i in top_list]

    def get_correlation_list(self):
        """
        获取相关性博文，最新创建的 3 个
        """
        # TODO: 通过 Cookie 获取用户最近点击标签，完成推荐部分
        correlation_list = Article.objects.filter(tag__contains='Python').order_by('-create_at').all()[0: 3]
        return [i.to_dict() for i in correlation_list]

    def get_by_id(self, article_id):
        """
        获取博客详细信息
        :param article_id: 博文 ID 号
        :return: 详细信息
        """
        obj = Article.objects.get(id=article_id)
        detail_info = obj.to_dict()

        detail_info['content'] = '博文内容有待补充'

        if os.path.exists(obj.content_path):
            with open(obj.content_path, 'r') as f:
                detail_info['content'] = markdown.markdown(f.read(), extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                    'markdown.extensions.toc',
                ])

        obj.pv_count += 1
        obj.save()

        return detail_info
