# coding=utf-8

import markdown

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
