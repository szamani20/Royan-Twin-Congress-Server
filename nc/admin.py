from django.contrib import admin

from nc.models import *
from royan.AdminBase import *


# admin.site.unregister(User)
# admin.site.unregister(Group)

class ISAbstractInline(admin.StackedInline):
    model = ISAbstract
    extra = 1
    min_num = 1
    max_num = 1


class OPAbstractInline(admin.StackedInline):
    model = OPAbstract
    extra = 1
    min_num = 1
    max_num = 1


class PosterAbstractInline(admin.StackedInline):
    model = PosterAbstract
    extra = 1
    min_num = 1
    max_num = 1


@admin.register(ISSpeaker)
class ISAdmin(ISAdminBase):
    inlines = [ISAbstractInline, ]


@admin.register(OPSpeaker)
class OPAdmin(OPAdminBase):
    inlines = [OPAbstractInline, ]


@admin.register(Poster)
class PosterAdmin(PosterAdminBase):
    inlines = [PosterAbstractInline, ]
