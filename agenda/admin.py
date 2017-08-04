from django.contrib import admin

from agenda.models import Event


@admin.register(Event)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('speaker_name', 'event_time', 'event_venue')
    list_filter = ('speaker_name', 'event_time', 'event_venue')
    search_fields = ('name', 'event_time', 'event_venue')
    fields = ('speaker_name', 'topic', 'event_time',
              'event_venue')
    ordering = ('event_time',)
