# coding=utf-8

from django.contrib import admin
import console.views as Index
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from apps.blog.views import Article as blog

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'mdeditor/', include('mdeditor.urls')),
    url(r'^console/', Index.Index.as_view()),
    url(r'^load_tags_info/', Index.Tags.as_view()),
    url(r'^load_blog_page/', Index.Blog.as_view()),
    url(r'^article_\d+', blog.as_view()),
]
