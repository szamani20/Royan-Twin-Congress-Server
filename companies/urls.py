from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^alive/$', alive, name='alive'),
    url(r'^all_companies/$', all_companies, name='all_companies'),
]
