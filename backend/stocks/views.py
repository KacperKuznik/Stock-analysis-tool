from django.http import HttpResponse

from .models import KlineEntry

def get_data(request, symbol):
    return HttpResponse("You're getting " + symbol)


def update(request, symbol):
    return HttpResponse("You're updating " + symbol)