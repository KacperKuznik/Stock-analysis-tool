from django.contrib import admin

# Register your models here.

from .models import KlineEntry, Symbol
admin.site.register(KlineEntry)
admin.site.register(Symbol)