from django.db import models


class Event(models.Model):
    speaker_name = models.CharField(max_length=100)
    topic = models.CharField(max_length=250)
    event_time = models.DateTimeField()
    event_venue = models.CharField(max_length=200)

    def get_json(self):
        return {
            'id': self.pk,
            'name': self.speaker_name,
            'topic': self.topic,
            'time': self.event_time.ctime() if self.time else self.time,
            'venue': self.event_venue
        }
