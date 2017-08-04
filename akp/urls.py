from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^alive/$', alive, name='alive'),
    url(r'^all_winners/$', all_winners, name='all_winners'),
    url(r'^all_national_winners/$', all_national_winners, name='all_national_winners'),
    url(r'^all_international_winners/$', all_international_winners, name='all_international_winners'),
    url(r'^kazemi_winner/$', kazemi_winner, name='kazemi_winner'),
    url(r'^fetch/$', fetch, name='fetch'),
]
