from django.db.models.signals import post_save
from django.dispatch import receiver

from royan.send_push import send_push
from scc.models import ISSpeaker, OPSpeaker, Poster


@receiver(post_save, sender=ISSpeaker)
def iss_signal(sender, instance, **kwargs):
    print('Received Signal: ', instance.name)
    send_push('speaker', 'scc', 'is', instance.pk)


@receiver(post_save, sender=OPSpeaker)
def op_signal(sender, instance, **kwargs):
    print('Received Signal: ', instance.name)
    send_push('speaker', 'scc', 'op', instance.pk)


@receiver(post_save, sender=Poster)
def poster_signal(sender, instance, **kwargs):
    print('Received Signal: ', instance.name)
    send_push('speaker', 'scc', 'poster', instance.pk)
