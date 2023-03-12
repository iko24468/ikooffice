from django.urls import path, re_path
from . import views

app_name = 'events'

urlpatterns = [
    path("", views.index, name="index"),
    path('genpdf/', views.genpdf, name='generate-pdf-file'),
    path("gentext/", views.gen_text, name='generate-text-file'),
    path("gencsv/", views.gen_csv, name='generate-csv-file'),
    path("getsubs/", views.list_subscribers, name='list-subscribers'),
    path('<country>/<state>/<city>/',views.tst, name='tst'),
    path("add_venue/", views.add_venue, name='add-venue'),
    path("events/", views.all_events, name='show-events'),
]
