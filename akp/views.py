import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from akp.models import NationalWinner, InternationalWinner


def alive(request):
    return HttpResponse(timezone.localtime(timezone.now()))


def all_winners(request):
    nw = list(NationalWinner.objects.all().order_by('pk'))
    iw = list(InternationalWinner.objects.all().order_by('pk'))
    data = [s.get_json() for s in nw] + [s.get_json() for s in iw]
    return JsonResponse(data=data,
                        safe=False)


def all_national_winners(request):
    ac = list(NationalWinner.objects.all().order_by('pk'))
    data = [s.get_json() for s in ac]
    return JsonResponse(data=data,
                        safe=False)


def all_international_winners(request):
    ac = list(InternationalWinner.objects.all().order_by('pk'))
    data = [s.get_json() for s in ac]
    return JsonResponse(data=data,
                        safe=False)


@csrf_exempt
def fetch(request):
    data = json.loads(request.body.decode('utf-8'))
    model_type = data.get('model_type', 'UNKNOWN')
    start_id = data.get('start_id', '10000')
    end_id = data.get('end_id', '-10000')
    res = []

    if model_type == 'NW':
        res = list(map(lambda x: x.get_json(),
                       list(NationalWinner.objects.filter(
                           pk__gte=start_id, pk__lte=end_id).order_by('pk'))))
    elif model_type == 'IW':
        res = list(map(lambda x: x.get_json(),
                       list(InternationalWinner.objects.filter(
                           pk__gte=start_id, pk__lte=end_id).order_by('pk'))))

    return JsonResponse(data=res, safe=False)
