from django.conf.urls import url
from main.handlers import create_handler, edit_handler
from main.views import initial_view

urlpatterns = [
    url(r'^create/$', create_handler),
    url(r'^edit/$', edit_handler),
    url(r'', initial_view)
]
