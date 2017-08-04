from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone

from agenda.models import Event


def alive(request):
    return HttpResponse(timezone.localtime(timezone.now()))


def all_events(request):
    es = list(Event.objects.all())
    data = [s.get_json() for s in es]
    return JsonResponse(data=data,
                        safe=False)

