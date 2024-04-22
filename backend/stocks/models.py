from django.db import models


class Symbol(models.Model):
    symbol = models.CharField(max_length=30)

    def __str__(self):
        return self.symbol
    
class KlineEntry(models.Model):
    symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE)
    open_time = models.DateTimeField("open time")
    open_price = models.FloatField(default=0.0)
    high_price = models.FloatField(default=0.0)
    low_price = models.FloatField(default=0.0)
    close_price = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0)
    close_time = models.DateTimeField("close time")
    number_of_trades = models.IntegerField(default=0)