# coding=utf-8

from django.views.generic import View
from django.shortcuts import render_to_response
from django.template import RequestContext
from console.common.logger import getLogger

__author__ = 'Sabiner'
log = getLogger()


class FeedBack(View):
    """
    Deal with feedback commit from visitor.
    """
    def get(self, *args, **kwargs):
        return render_to_response('feedback/feedback.html')

    def post(self, request):
        log.debug(dir(request))
        log.debug(request.content_params)
        content = {
            'state': 'ok'
        }
        return render_to_response('feedback/feedback.html', content)
