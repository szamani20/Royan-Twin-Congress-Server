from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^alive/$', alive, name='alive'),
    url(r'^all_events/$', all_events, name='all_events'),
    url(r'^fetch/$', fetch, name='fetch'),
]
