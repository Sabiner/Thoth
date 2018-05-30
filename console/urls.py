# coding=utf-8

import console.views as Index
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^console/', Index.Index.as_view()),
    url(r'^load_tags_info/', Index.Tags.as_view()),
    url(r'^load_blog_page/', Index.Blog.as_view()),
)
