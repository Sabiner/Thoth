
from django.conf.urls import url
from .views import GuestBookView

urlpatterns = [
    url(r'^message_board?$', GuestBookView.as_view({'get': 'message_board'}), name='message_board'),
    url(r'^leave_word?$', GuestBookView.as_view({'post': 'leave_word'}), name='leave_word'),
    url(r'^load_guest_book?$', GuestBookView.as_view({'get': 'load_guest_book'}), name='load_guest_book')
]
