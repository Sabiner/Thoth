# coding=utf-8

from django.contrib import admin
import console.views as Index
from django.conf.urls import url, include
from django.conf.urls.static import static
from apps.blog import views as blog
from apps.account.views import FeedBack as feedback
import settings

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'mdeditor/', include('mdeditor.urls')),
    url(r'^$', Index.Index.as_view()),
    url(r'^load_tags_info', Index.Tags.as_view()),
    url(r'^load_blog_page', Index.Blog.as_view()),
    url(r'^article', blog.Article.as_view()),
    url(r'^feedback', feedback.as_view()),
    url(r'^show_type', blog.Tag.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
