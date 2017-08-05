from django.db import models

from royan.ModelBase import Company


class OrdinaryCompanyPictures(models.Model):
    image = models.ImageField(upload_to='images/company/bulk/')
    company = models.ForeignKey('OrdinaryCompany')


class SponsorCompanyPictures(models.Model):
    image = models.ImageField(upload_to='images/company/bulk/')
    company = models.ForeignKey('SponsorCompany')


class SponsorCompany(Company):
    class Meta:
        verbose_name = 'Sponsor Company'

    def get_json(self):
        return {
            'id': self.pk,
            'name': self.name,
            'logo': 'https://royan.szamani.ir' + self.logo.url if self.logo and self.logo.url else '',
            'location': self.location,
            'pics': [
                'https://royan.szamani.ir' + i.image.url if i.image and i.image.url else ''
                for i in list(self.sponsorcompanypictures_set.all())
                ],
            'website': self.website,
            'phone': self.phone,
            'address': self.address,
            'type': 0
        }


class OrdinaryCompany(Company):
    class Meta:
        verbose_name = 'Non Sponsor Company'

    def get_json(self):
        return {
            'id': self.pk,
            'name': self.name,
            'logo': 'https://royan.szamani.ir' + self.logo.url if self.logo and self.logo.url else '',
            'location': self.location,
            'pics': [
                'https://royan.szamani.ir' + i.image.url if i.image and i.image.url else ''
                for i in list(self.ordinarycompanypictures_set.all())
                ],
            'website': self.website,
            'phone': self.phone,
            'address': self.address,
            'type': 1
        }
