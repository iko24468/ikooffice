from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import date
import calendar
from calendar import HTMLCalendar
from .forms import VenueForm
from django.http import FileResponse
from django.template.response import TemplateResponse
import csv
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.core.paginator import Paginator
from .models import Event, Venue, MyClubUser


def list_subscribers(request):
    p = Paginator(MyClubUser.objects.all(), 3)
    page = request.GET.get('page')
    subscribers = p.get_page(page)
    return render(request, 'events/subscribers.html', {'subscribers': subscribers})


def genpdf(request):
    buf =io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica-Oblique", 14)
    lines = [
        "I will not expose the ignorance of the faculty",
        "I will not conduct my own fire drills",
        "I will not prescribe medication",
    ]
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='bart.pdf')


def gen_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; file_name="bart.txt"'
    lines = [
        "I will not expose the ignorance of the faculty.\n",
        "I will not conduct my own fire drills.\n",
        "I will not prescribe medication.\n",
    ]
    response.writelines(lines)
    return response


def gen_csv(reqeust):
    response = HttpResponse(content_type='text/csv')
    response['Content_disposition'] = 'attachment; filename = "venues.csv"'
    writer = csv.writer(response)
    venues = Venue.venues.all()
    writer.writerow(['Venue Name', 'address', 'Phone', 'Email'])
    for venue in venues:
        writer.writerow([venue.name, venue.address, venue.phone, venue.email_address])
    return response


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html', {'event_list': event_list})


def index(request, year=date.today().year, month=date.today().month):
    # usr = request.user
    # ses = request.session
    # path = request.path
    # path_info = request.path_info
    # headers = request.headers
    # assert False
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
    # return render(request,
    #               'events/calendar_base.html',
    #               {'title': title, 'cal': cal, 'announcements': announcements}
    #               )
    return TemplateResponse(request, 'events/calendar_base.html',
                            {'title': title, 'cal': cal, 'announcements': announcements})



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
