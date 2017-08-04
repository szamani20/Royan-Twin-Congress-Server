from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from akp.models import NationalWinner, InternationalWinner


def alive(request):
    return HttpResponse(timezone.localtime(timezone.now()))


def all_winners(request):
    nw = list(NationalWinner.objects.all())
    iw = list(InternationalWinner.objects.all())
    data = [s.get_json() for s in nw] + [s.get_json() for s in iw]
    return JsonResponse(data=data,
                        safe=False)


def all_national_winners(request):
    ac = list(NationalWinner.objects.all())
    data = [s.get_json() for s in ac]
    return JsonResponse(data=data,
                        safe=False)


def all_international_winners(request):
    ac = list(InternationalWinner.objects.all())
    data = [s.get_json() for s in ac]
    return JsonResponse(data=data,
                        safe=False)


def kazemi_winner(request):
    kw = InternationalWinner.objects.filter(kazemi=True).first()
    if not kw:
        return JsonResponse(data={},
                            safe=False)
    data = kw.get_json()
    return JsonResponse(data=data,
                        safe=False)


@csrf_exempt
def fetch(request):
    model_type = request.POST.get('model_type', 'UNKNOWN')
    start_id = request.POST.get('start_id', '-1')
    end_id = request.POST.get('end_id', '-1')
    res = []

    if model_type == 'NW':
        res = list(map(lambda x: x.get_json(),
                       list(NationalWinner.objects.filter(
                           pk__gte=start_id, pk__lte=end_id))))
    elif model_type == 'IW':
        res = list(map(lambda x: x.get_json(),
                       list(InternationalWinner.objects.filter(
                           pk__gte=start_id, pk__lte=end_id))))

    return JsonResponse(data=res, safe=False)
