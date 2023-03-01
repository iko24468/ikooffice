from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import date
import calendar
from calendar import HTMLCalendar
from .models import Event
from .forms import VenueForm


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html', {'event_list': event_list})


def index(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 1900 or year > 2099:
        year = date.today().year
    month_name = calendar.month_name[month]
    title = "MyClub Event Calendar - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    announcements = [
        {
            'date': '6-10-2020',
            'announcement': "Club Registrations Open"
        },
        {
            'date': '6-15-2020',
            'announcement': "Joe Smith Elected New Club President"
        }
    ]
    return render(request,
                  'events/calendar_base.html',
                  {'title': title, 'cal': cal, 'announcements': announcements}
                  )


def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue/?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(
        request,
        'events/add_venue.html',
        {'form': form, 'submitted': submitted}
    )

def tst(request, country, state, city):

    return render(
        request,
        'snslaw/mytest.html', {'country': country})
