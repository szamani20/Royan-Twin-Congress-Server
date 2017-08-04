from django.db import models


class Event(models.Model):
    speaker_name = models.CharField(max_length=100)
    topic = models.CharField(max_length=250)
    event_time = models.DateTimeField()
    event_venue = models.CharField(max_length=200)

    def get_json(self):
        return {
            'speaker_name': self.speaker_name,
            'topic': self.topic,
            'event_time': self.event_time.ctime(),
            'event_venue': self.event_venue
        }
