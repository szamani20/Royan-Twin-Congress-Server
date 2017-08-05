from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from companies.models import SponsorCompany, OrdinaryCompany


def alive(request):
    return HttpResponse(timezone.localtime(timezone.now()))


def sp_company(request):
    all_is_speakers = list(SponsorCompany.objects.all())
    data = [s.get_json() for s in all_is_speakers]
    return JsonResponse(data=data,
                        safe=False)


def or_company(request):
    all_is_speakers = list(OrdinaryCompany.objects.all())
    data = [s.get_json() for s in all_is_speakers]
    return JsonResponse(data=data,
                        safe=False)


@csrf_exempt
def fetch(request):
    model_type = request.POST.get('model_type', 'UNKNOWN')
    start_id = request.POST.get('start_id', '-1')
    end_id = request.POST.get('end_id', '-1')
    res = []

    if model_type == 'SP':
        res = list(map(lambda x: x.get_json(),
                       list(SponsorCompany.objects.filter(
                           pk__gte=start_id, pk__lte=end_id))))
    elif model_type == 'OR':
        res = list(map(lambda x: x.get_json(),
                       list(OrdinaryCompany.objects.filter(
                           pk__gte=start_id, pk__lte=end_id))))

    return JsonResponse(data=res, safe=False)
