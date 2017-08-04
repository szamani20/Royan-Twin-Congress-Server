from django.db.models.signals import post_save
from django.dispatch import receiver

from scc.models import ISSpeaker, OPSpeaker, Poster


@receiver(post_save, sender=ISSpeaker)
def add_to_changes(sender, instance, **kwargs):
    # TODO: request to push notification service
    print('Heloo signal \n\n\n')
    print(sender)
    print(instance)
