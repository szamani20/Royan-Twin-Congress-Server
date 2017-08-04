from django.contrib import admin

from akp.models import NationalWinnerAbstract, InternationalWinnerAbstract, NationalWinner, InternationalWinner
from royan.AdminBase import WinnerAdminBase


class NationalWinnerAbstractInline(admin.StackedInline):
    model = NationalWinnerAbstract
    extra = 1
    min_num = 1
    max_num = 1


class InternationalWinnerAbstractInline(admin.StackedInline):
    model = InternationalWinnerAbstract
    extra = 1
    min_num = 1
    max_num = 1


@admin.register(NationalWinner)
class NWAdmin(WinnerAdminBase):
    inlines = [NationalWinnerAbstractInline, ]


@admin.register(InternationalWinner)
class IWAdmin(WinnerAdminBase):
    inlines = [InternationalWinnerAbstractInline, ]
