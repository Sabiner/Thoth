# coding=utf-8

import markdown
import chardet

from django.views.generic import View
from console.common.logger import getLogger
from django.shortcuts import render_to_response
from service import ArticleService

log = getLogger()


class Article(View):

    def get(self, *args, **kwargs):
        url, blog = None, dict()
        try:
            blog_url = args[0].path
            url = blog_url.split('/')[-1]
        except IndexError, e:
            log.debug(e)

        log.debug(url)
        if url:
            blog = ArticleService.get_blog_by_url(url)

        content = unicode(blog['content'], 'utf-8')
        blog['content'] = markdown.markdown(content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])

        params = {'blog': blog}
        return render_to_response('article/show.html', params)


class Tag(View):

    def get(self, *args, **kwargs):
        params = dict()

        path_info = args[0].get_full_path()
        _type = path_info.split('=')[-1]

        start = 0
        end = 12

        params['type'] = _type
        articles = ArticleService.get_blog_by_type(_type, start, end)

        params['articles'] = articles
        return render_to_response('tag/show.html', params)
