from django.contrib import admin

speaker_display = ('name', 'email', 'country', 'topic')
winner_display = ('name', 'email', 'country', 'award_time',
                  'award_venue', )
company_display = ('name', 'website', 'phone', 'location')


class ISAdminBase(admin.ModelAdmin):
    list_display = speaker_display
    list_filter = speaker_display
    search_fields = speaker_display
    fields = ('name', 'email', 'country', 'avatar', 'affiliation',
              'topic', 'time', 'venue')
    ordering = ('name',)


class OPAdminBase(admin.ModelAdmin):
    list_display = speaker_display
    list_filter = speaker_display
    search_fields = speaker_display
    fields = ('name', 'email', 'country', 'avatar', 'affiliation',
              'topic', 'time', 'venue')
    ordering = ('name',)


class PosterAdminBase(admin.ModelAdmin):
    list_display = speaker_display
    list_filter = speaker_display
    search_fields = speaker_display
    fields = ('name', 'email', 'country', 'avatar', 'affiliation',
              'topic', 'time', 'venue')
    ordering = ('name',)


class WinnerAdminBase(admin.ModelAdmin):
    list_display = winner_display
    list_filter = winner_display
    search_fields = ('name', 'email', 'country', 'award_time',
                     'award_venue')
    fields = ('name', 'avatar', 'email', 'affiliation',
              'country', 'short_cv',
              'award_time', 'award_venue',)
    ordering = ('award_time',)


class CompanyAdminBase(admin.ModelAdmin):
    list_display = company_display
    list_filter = company_display
    search_fields = company_display
    fields = ('name', 'logo', 'location',
              'website', 'description', 'phone', 'address')
    ordering = ('name',)
