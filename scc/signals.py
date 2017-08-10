from django.db.models.signals import post_save
from django.dispatch import receiver

from royan.send_push import send_push
from scc.models import ISSpeaker, OPSpeaker, Poster


@receiver(post_save, sender=ISSpeaker)
def iss_signal(sender, instance, **kwargs):
    print('Received Signal: ', instance.name)
    send_push('speaker', 'IS', instance.pk)


@receiver(post_save, sender=OPSpeaker)
def op_signal(sender, instance, **kwargs):
    print('Received Signal: ', instance.name)
    send_push('speaker', 'OP', instance.pk)


@receiver(post_save, sender=Poster)
def poster_signal(sender, instance, **kwargs):
    print('Received Signal: ', instance.name)
    send_push('speaker', 'POSTER', instance.pk)
