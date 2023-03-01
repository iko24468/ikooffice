from django.contrib import admin
from .models import MyClubUser, Event, Venue
from snslaw.models import MyClient, ClientFiles, Publisher


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # fields = (('name', 'venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)
    fieldsets = (
        ('required information', {
            'description': "These fields are required for each event.",
            'fields': (('name', 'venue'), 'event_date')
        }),
        ('optional information', {
            'classes': ('collapse',),
            'fields': ('description', 'manager')
        }),
    )


admin.site.register(MyClubUser)
admin.site.register(MyClient)
admin.site.register(ClientFiles)
admin.site.register(Publisher)

