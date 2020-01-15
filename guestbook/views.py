# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
from rest_framework import viewsets
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from guestbook.models import GuestBook
from Thoth.utils import load_logger

logger = load_logger()


class GuestBookView(viewsets.ViewSet):

    def message_board(self, request):
        """
        加载留言板界面
        """
        return render(request, 'guestbook/leave_word.html')

    @csrf_exempt
    def leave_word(self, request):
        """
        保存留言
        :param request: 留言内容
        :return: 保存成功或失败
        """
        result = dict(code=0, msg='')
        try:
            message = ''
            if 'message' in request.data:
                message = request.data.get('message').strip()

            if message:
                GuestBook.objects.create(**dict(message=message, creator='匿名用户'))
            else:
                result['code'] = 1
                result['msg'] = '请填写内容'
        except Exception as e:
            err = sys.exc_info()[0]
            err_type, err_args = err, err.args

            result['code'] = 1
            result['msg'] = f'{err_type}: {err_args}'

        logger.info(result)
        return HttpResponse(result)

    def load_guest_book(self, request):
        """
        留言板列表展示
        :param request: 请求
        :return: 响应
        """
        response = dict(messages=[])
        try:
            messages = GuestBook.objects.all().order_by('-create_at')[0: 10]

            if messages:
                response['messages'] = [i.to_dict() for i in messages]
        except Exception as e:
            response['messages'] = e.message

        return render(request, 'guestbook/guest_book.html', response)
