# coding=utf-8

from django.views.generic import View
from console.common.logger import getLogger
from django.shortcuts import render_to_response

log = getLogger()


class Article(View):
    def get(self, *args, **kwargs):
        log.debug('---------------------')
        log.debug(args)
        log.debug(kwargs)
        return render_to_response('article/show.html')
