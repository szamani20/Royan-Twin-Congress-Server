import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from rbc.models import ISSpeaker, OPSpeaker, Poster


def alive(request):
    return HttpResponse(timezone.localtime(timezone.now()))


def is_speaker(request):
    all_is_speakers = list(ISSpeaker.objects.all())
    data = [s.get_json() for s in all_is_speakers]
    return JsonResponse(data=data,
                        safe=False)


def op_speaker(request):
    all_is_speakers = list(OPSpeaker.objects.all())
    data = [s.get_json() for s in all_is_speakers]
    return JsonResponse(data=data,
                        safe=False)


def poster(request):
    all_is_speakers = list(Poster.objects.all())
    data = [s.get_json() for s in all_is_speakers]
    return JsonResponse(data=data,
                        safe=False)


@csrf_exempt
def fetch(request):
    data = json.loads(request.body.decode('utf-8'))
    model_type = data.get('model_type', 'UNKNOWN')
    start_id = data.get('start_id', '-1')
    end_id = data.get('end_id', '-1')
    res = []

    if model_type == 'IS':
        res = list(map(lambda x: x.get_json(),
                       list(ISSpeaker.objects.filter(
                           pk__gte=start_id, pk__lte=end_id))))
    elif model_type == 'OP':
        res = list(map(lambda x: x.get_json(),
                       list(OPSpeaker.objects.filter(
                           pk__gte=start_id, pk__lte=end_id))))
    elif model_type == 'Poster':
        res = list(map(lambda x: x.get_json(),
                       list(Poster.objects.filter(
                           pk__gte=start_id, pk__lte=end_id))))

    return JsonResponse(data=res, safe=False)
