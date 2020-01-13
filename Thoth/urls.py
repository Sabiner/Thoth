from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from Thoth.views import Index

urlpatterns = [
    url(r'^$', Index.as_view({'get': 'get'})),
    url(r'^admin/', admin.site.urls),
    url(r'mdeditor/', include('mdeditor.urls')),
    url(r'^article/', include('article.urls'), name='article'),
    url(r'^about_me?$', Index.as_view({'get': 'about_me'}), name='about_me'),
    url(r'^guestbook/', include('guestbook.urls'), name='guestbook'),
    url(r'^pigeonhole?$', Index.as_view({'get': 'pigeonhole'}), name='pigeonhole')
]

if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
