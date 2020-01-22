from django.contrib import admin
from .models import Venue, Agency, Genre, Author, Issue, Party, Level, Event, Politician, Local_Link, District, Category, Organization, Program, Bureaucrat, Story, Blog, Report_Link, Media_Org
##NodaSF###

    
class VenueAdmin(admin.ModelAdmin):
    list_display = ['name' ]

class AgencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']

class OrgAdmin(admin.ModelAdmin):
    list_display = ['name', 'issue', 'category']

class PoliticianAdmin(admin.ModelAdmin):
    list_display = ['last_name','first_name', 'district', 'level', 'candidate',]
    
class BureaucratAdmin(admin.ModelAdmin):
    list_display = ['last_name','first_name', 'organization',]    

admin.site.register(Story)
admin.site.register(Author)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Agency, AgencyAdmin)
admin.site.register(Genre)
admin.site.register(Issue)
admin.site.register(Blog)
admin.site.register(Party)
admin.site.register(Level)
admin.site.register(Report_Link)
admin.site.register(Politician, PoliticianAdmin)
admin.site.register(Local_Link)
admin.site.register(Media_Org)
admin.site.register(District)
admin.site.register(Category)
admin.site.register(Organization, OrgAdmin)
admin.site.register(Bureaucrat, BureaucratAdmin)
admin.site.register(Program)
