from django.urls import path, re_path
from . import views

app_name = 'events'

urlpatterns = [
    path("", views.index, name="index"),
    path('<country>/<state>/<city>/',views.tst, name='tst'),
    path("add_venue/", views.add_venue, name='add-venue'),
    path("events/", views.all_events, name='show-events'),
]