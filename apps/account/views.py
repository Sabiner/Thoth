# coding=utf-8

from django.views.generic import View
from django.shortcuts import render_to_response

__author__ = 'Sabiner'


class FeedBack(View):
    """
    Deal with feedback commit from visitor.
    """
    def get(self, *args, **kwargs):
        return render_to_response('feedback/feedback.html')

    def post(self):
        return render_to_response('feedback/feedback.html')
