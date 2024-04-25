from django.http import HttpResponse, JsonResponse
from scripts import get_binance_data
from .models import KlineEntry
from datetime import datetime
def get_data(request, symbol):
    data = get_binance_data.run()
    res = []
    for row in data:
        record = {}
        record["x"] = datetime.fromtimestamp(row[0] // 1000)
        record["y"] = row[1:5]
        res.append(record)
    return JsonResponse({"data": res})


def update(request, symbol):
    return HttpResponse("You're updating " + symbol)