
from django.conf.urls import url
from .views import PigeonholeView

urlpatterns = [
    url(r'^$', PigeonholeView.as_view({'get': 'get_page'}), name='get_page'),
    url(r'^get_items_by_tag?$', PigeonholeView.as_view({'get': 'get_items_by_tag'}), name='get_items_by_tag'),
]
