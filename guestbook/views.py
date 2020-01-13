# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
                GuestBook.objects.create(**dict(message=message))
            else:
                result['code'] = 1
                result['msg'] = '请填写内容'
        except Exception as e:
            result['code'] = 1
            result['msg'] = e.message

        return HttpResponse(result)

    def load_guest_book(self, request):
        """
        留言板列表展示
        :param request: 请求
        :return: 响应
        """
        response = dict(messages=[])
        try:
            logger.info("coming in load guestbook")
            messages = GuestBook.objects.all().order_by('-create_at')[0: 10]
            logger.info(messages)
            if messages:
                response['messages'] = [i.to_dict() for i in messages]
        except Exception as e:
            response['messages'] = e.message
        logger.info(response)
        return render(request, 'guestbook/guest_book.html', response)
