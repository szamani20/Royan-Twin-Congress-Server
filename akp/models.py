from django.db import models

from royan.ModelBase import Abstract, Winner


class NationalWinnerAbstract(Abstract):
    winner = models.ForeignKey('NationalWinner',
                               on_delete=models.CASCADE,
                               unique=True)

    class Meta:
        abstract = False
        managed = True


class InternationalWinnerAbstract(Abstract):
    winner = models.ForeignKey('InternationalWinner',
                               on_delete=models.CASCADE,
                               unique=True)

    class Meta:
        abstract = False
        managed = True


class NationalWinner(Winner):
    class Meta:
        verbose_name = 'National Winner'

    def get_json(self):
        return {'id': self.pk,
                'type': 1,
                'name': self.name,
                'avatar': 'https://royan.szamani.ir' + self.avatar.url if self.avatar and self.avatar.url else '',
                'email': self.email,
                'affiliation': self.affiliation,
                'country': self.country,
                'short_cv': self.short_cv,
                'award_time': self.award_time.ctime(),
                'award_venue': self.award_venue,
                'kazemi': self.kazemi,
                'aabstract': {'id': self.pk,
                              'background': self.nationalwinnerabstract_set.first().background,
                              'objective': self.nationalwinnerabstract_set.first().objective,
                              'method': self.nationalwinnerabstract_set.first().method,
                              'result': self.nationalwinnerabstract_set.first().result,
                              'conclusion': self.nationalwinnerabstract_set.first().conclusion,
                              'keyword': self.nationalwinnerabstract_set.first().keyword,
                              } if self.nationalwinnerabstract_set.first() else '',
                }


class InternationalWinner(Winner):
    class Meta:
        verbose_name = 'International Winner'

    def get_json(self):
        return {'id': self.pk,
                'type': 0,
                'name': self.name,
                'avatar': 'https://royan.szamani.ir' + self.avatar.url if self.avatar and self.avatar.url else '',
                'email': self.email,
                'affiliation': self.affiliation,
                'country': self.country,
                'short_cv': self.short_cv,
                'award_time': self.award_time.ctime(),
                'award_venue': self.award_venue,
                'kazemi': self.kazemi,
                'aabstract': {
                    'background': self.internationalwinnerabstract_set.first().background,
                    'objective': self.internationalwinnerabstract_set.first().objective,
                    'method': self.internationalwinnerabstract_set.first().method,
                    'result': self.internationalwinnerabstract_set.first().result,
                    'conclusion': self.internationalwinnerabstract_set.first().conclusion,
                    'keyword': self.internationalwinnerabstract_set.first().keyword,
                } if self.internationalwinnerabstract_set.first() else '',
                }
