# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
import os
from django.contrib import admin
from .models import GuestBook


@admin.register(GuestBook)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('message', 'creator', 'create_at')  # 列表展示
    search_fields = ('message', 'creator')    # 搜索
    list_filter = ('message', 'creator')       # 过滤
