# coding=utf-8
"""
Index view
"""
from django.views.generic import View
from django.shortcuts import render_to_response
from django.http.response import HttpResponse


class Index(View):
    def get(self, request, *args, **kwargs):
        #return HttpResponse('hello world')
        return render_to_response('index/index.html', {'index': 'Hello world'})
