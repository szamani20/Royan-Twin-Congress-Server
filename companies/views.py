from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone

from companies.models import Company


def alive(request):
    return HttpResponse(timezone.localtime(timezone.now()))


def all_companies(request):
    ac = list(Company.objects.all())
    data = [s.get_json() for s in ac]
    return JsonResponse(data=data,
                        safe=False)
