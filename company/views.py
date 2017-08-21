import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from company.models import SponsorCompany, OrdinaryCompany


def alive(request):
    return HttpResponse(timezone.localtime(timezone.now()))


def sp_company(request):
    all_is_speakers = list(SponsorCompany.objects.all().order_by('pk'))
    data = [s.get_json() for s in all_is_speakers]
    return JsonResponse(data=data,
                        safe=False)


def or_company(request):
    all_is_speakers = list(OrdinaryCompany.objects.all().order_by('pk'))
    data = [s.get_json() for s in all_is_speakers]
    return JsonResponse(data=data,
                        safe=False)


@csrf_exempt
def fetch(request):
    data = json.loads(request.body.decode('utf-8'))
    model_type = data.get('model_type', 'UNKNOWN')
    start_id = data.get('start_id', '10000')
    end_id = data.get('end_id', '-10000')
    res = []

    if model_type == 'SP':
        res = list(map(lambda x: x.get_json(),
                       list(SponsorCompany.objects.filter(
                           pk__gte=start_id, pk__lte=end_id).order_by('pk'))))
    elif model_type == 'OR':
        res = list(map(lambda x: x.get_json(),
                       list(OrdinaryCompany.objects.filter(
                           pk__gte=start_id, pk__lte=end_id).order_by('pk'))))

    return JsonResponse(data=res, safe=False)
