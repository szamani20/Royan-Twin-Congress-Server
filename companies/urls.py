from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^alive/$', alive, name='alive'),
    url(r'^all_sp_company/$', sp_company, name='all_companies'),
    url(r'^all_or_company/$', or_company, name='all_companies'),
    url(r'^fetch/$', fetch, name='fetch'),
]
