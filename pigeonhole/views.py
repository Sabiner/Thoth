# coding: utf-8

from collections import Counter
from django.shortcuts import render

from rest_framework import viewsets
from article.models import Article
from Thoth.utils import load_logger

logger = load_logger()


class PigeonholeView(viewsets.ViewSet):

    def get_page(self, request):
        all_tags = self.get_all_tags()
        response = dict(
            all_tags=dict(all_tags)
        )
        return render(request, 'pigeonhole/pigeonhole.html', response)

    def get_items_by_tag(self, request):
        """
        根据指定标签名获取最近时间内创建的博文
        TODO：支持分页控制
        :param request: 分页信息
        :param tag_name 标签名
        :return: 博文集合
        """
        response = None
        try:
            tag_name = request.query_params.get('tag_name')
            if tag_name:
                items = Article.objects.filter(tag__contains=tag_name).order_by('-create_at').all()[0: 6]
                response = dict(
                    tag_name=tag_name,
                    articles=[i.to_dict() for i in items if items]
                )
        except Exception as e:
            logger.info(f'{e.args}')
        return render(request, 'pigeonhole/article_block.html', response)

    def get_all_tags(self):
        """
        获取所有标签
        :return:
        """
        tag_items = Article.objects.values("tag").all()
        tmp = [item['tag'] for item in tag_items]

        all_tags = []
        for tags in tmp:
            all_tags.extend([i.strip() for i in tags.split(',')])

        return Counter(all_tags)
