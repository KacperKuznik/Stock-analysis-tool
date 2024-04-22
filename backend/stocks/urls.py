from django.urls import path

from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    path("<str:symbol>/", views.get_data, name="get_data"),
    path("<str:symbol>/update", views.update, name="update"),
]