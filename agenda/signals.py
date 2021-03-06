from django.db.models.signals import post_save
from django.dispatch import receiver

from royan.send_push import send_push
from agenda.models import Event


@receiver(post_save, sender=Event)
def sponsor_signal(sender, instance, **kwargs):
    print('Received Signal: ', instance.speaker_name)
    send_push('event', None, None, instance.pk)
