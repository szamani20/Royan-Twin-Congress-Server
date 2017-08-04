"""royan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^scc/', include('scc.urls', namespace='scc')),
    url(r'^rbc/', include('rbc.urls', namespace='rbc')),
    url(r'^nc/', include('nc.urls', namespace='nc')),
    url(r'^companies/', include('companies.urls', namespace='companies')),
    url(r'^akp/', include('akp.urls', namespace='akp')),
    url(r'^agenda/', include('agenda.urls', namespace='agenda')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)