# coding=utf-8

from django.contrib import admin
import console.views as Index
from django.conf.urls import url, include
from apps.blog import views as blog
from apps.account.views import FeedBack as feedback

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'mdeditor/', include('mdeditor.urls')),
    url(r'^console/', Index.Index.as_view()),
    url(r'^load_tags_info/', Index.Tags.as_view()),
    url(r'^load_blog_page/', Index.Blog.as_view()),
    url(r'^article_\d+', blog.Article.as_view()),
    url(r'^feedback/', feedback.as_view()),
    url(r'^show_type', blog.Tag.as_view()),
]
