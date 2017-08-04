from django.contrib import admin

from companies.models import OrdinaryCompanyPictures, SponsorCompanyPictures, OrdinaryCompany, SponsorCompany
from royan.AdminBase import CompanyAdminBase


class OrdinaryCompanyPictureInline(admin.StackedInline):
    model = OrdinaryCompanyPictures
    extra = 1


class SponsorCompanyPictureInline(admin.StackedInline):
    model = SponsorCompanyPictures
    extra = 1


@admin.register(OrdinaryCompany)
class OrdinaryCompanyAdmin(CompanyAdminBase):
    inlines = [OrdinaryCompanyPictureInline, ]


@admin.register(SponsorCompany)
class SponsorCompanyAdmin(CompanyAdminBase):
    inlines = [SponsorCompanyPictureInline, ]
