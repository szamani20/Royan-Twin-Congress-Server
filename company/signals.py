from django.db.models.signals import post_save
from django.dispatch import receiver

from royan.send_push import send_push
from company.models import SponsorCompany, OrdinaryCompany


@receiver(post_save, sender=SponsorCompany)
def sponsor_signal(sender, instance, **kwargs):
    print('Received Signal: ', instance.name)
    send_push('company', 'sponsor', None, instance.pk)


@receiver(post_save, sender=OrdinaryCompany)
def ordinary_signal(sender, instance, **kwargs):
    print('Received Signal: ', instance.name)
    send_push('company', 'ordinary', None, instance.pk)
