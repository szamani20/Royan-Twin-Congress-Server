from django.db import models

from royan.ModelBase import Speaker, Abstract


class ISAbstract(Abstract):
    speaker = models.ForeignKey('ISSpeaker',
                                on_delete=models.CASCADE,
                                unique=True)

    class Meta:
        abstract = False
        managed = True


class OPAbstract(Abstract):
    speaker = models.ForeignKey('OPSpeaker',
                                on_delete=models.CASCADE,
                                unique=True)

    class Meta:
        abstract = False
        managed = True


class PosterAbstract(Abstract):
    speaker = models.ForeignKey('Poster',
                                on_delete=models.CASCADE,
                                unique=True)

    class Meta:
        abstract = False
        managed = True


class ISSpeaker(Speaker):
    class Meta:
        verbose_name = 'RBC Invited Speaker'

    def get_json(self):
        return {'id': self.pk,
                'congress': 1,
                'type': 0,
                'name': self.name,
                'email': self.email,
                'country': self.country,
                'avatar': 'https://royan.szamani.ir' + self.avatar.url if self.avatar and self.avatar.url else '',
                'affiliation': self.affiliation,
                'topic': self.topic,
                'time': self.time.ctime(),
                'venue': self.venue,
                'aabstract': {
                    'background': self.isabstract_set.first().background,
                    'objective': self.isabstract_set.first().objective,
                    'method': self.isabstract_set.first().method,
                    'result': self.isabstract_set.first().result,
                    'conclusion': self.isabstract_set.first().conclusion,
                    'keyword': self.isabstract_set.first().keyword,
                } if self.isabstract_set.first() else {
                    'background': '',
                    'objective': '',
                    'method': '',
                    'result': '',
                    'conclusion': '',
                    'keyword': '',
                },
                }


class OPSpeaker(Speaker):
    class Meta:
        verbose_name = 'RBC Oral Presentation'

    def get_json(self):
        return {'id': self.pk,
                'congress': 1,
                'type': 1,
                'name': self.name,
                'email': self.email,
                'country': self.country,
                'avatar': 'https://royan.szamani.ir' + self.avatar.url if self.avatar and self.avatar.url else '',
                'affiliation': self.affiliation,
                'topic': self.topic,
                'time': self.time.ctime(),
                'venue': self.venue,
                'aabstract': {
                    'background': self.opabstract_set.first().background,
                    'objective': self.opabstract_set.first().objective,
                    'method': self.opabstract_set.first().method,
                    'result': self.opabstract_set.first().result,
                    'conclusion': self.opabstract_set.first().conclusion,
                    'keyword': self.opabstract_set.first().keyword,
                } if self.opabstract_set.first() else {
                    'background': '',
                    'objective': '',
                    'method': '',
                    'result': '',
                    'conclusion': '',
                    'keyword': '',
                },
                }


class Poster(Speaker):
    class Meta:
        verbose_name = 'RBC Poster'

    def get_json(self):
        return {'id': self.pk,
                'congress': 1,
                'type': 2,
                'name': self.name,
                'email': self.email,
                'country': self.country,
                'avatar': 'https://royan.szamani.ir' + self.avatar.url if self.avatar and self.avatar.url else '',
                'affiliation': self.affiliation,
                'topic': self.topic,
                'time': self.time.ctime(),
                'venue': self.venue,
                'aabstract': {
                    'background': self.posterabstract_set.first().background,
                    'objective': self.posterabstract_set.first().objective,
                    'method': self.posterabstract_set.first().method,
                    'result': self.posterabstract_set.first().result,
                    'conclusion': self.posterabstract_set.first().conclusion,
                    'keyword': self.posterabstract_set.first().keyword,
                } if self.posterabstract_set.first() else {
                    'background': '',
                    'objective': '',
                    'method': '',
                    'result': '',
                    'conclusion': '',
                    'keyword': '',
                },
                }
