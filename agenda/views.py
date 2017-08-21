import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from agenda.models import Event


def alive(request):
    return HttpResponse(timezone.localtime(timezone.now()))


def all_events(request):
    es = list(Event.objects.all().order_by('pk'))
    data = [s.get_json() for s in es]
    return JsonResponse(data=data,
                        safe=False)


@csrf_exempt
def fetch(request):
    data = json.loads(request.body.decode('utf-8'))
    start_id = data.get('start_id', '10000')
    end_id = data.get('end_id', '-10000')
    res = list(map(lambda x: x.get_json(),
                   list(Event.objects.filter(
                       pk__gte=start_id, pk__lte=end_id).order_by('pk'))))

    return JsonResponse(data=res, safe=False)
