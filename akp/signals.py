from django.db.models.signals import post_save
from django.dispatch import receiver

from royan.send_push import send_push
from akp.models import NationalWinner, InternationalWinner


@receiver(post_save, sender=InternationalWinner)
def sponsor_signal(sender, instance, **kwargs):
    print('Received Signal: ', instance.name)
    send_push('winner', 'international', None, instance.pk)


@receiver(post_save, sender=NationalWinner)
def ordinary_signal(sender, instance, **kwargs):
    print('Received Signal: ', instance.name)
    send_push('winner', 'national', None, instance.pk)
