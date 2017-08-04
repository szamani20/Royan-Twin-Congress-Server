from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^alive/$', alive, name='alive'),
    url(r'^all_is_speaker/$', is_speaker, name='is_speaker'),
    url(r'^all_op_speaker/$', op_speaker, name='op_speaker'),
    url(r'^all_poster_speaker/$', poster, name='poster'),
    url(r'^fetch/$', fetch, name='fetch'),
]
