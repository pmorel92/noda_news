from django.contrib import admin
from .models import County, Venue, Agency, Genre, Issue, City, Party, Level, SF_Event, Politician, Local_Link, District, Category, Organization, Program, Bureaucrat
##NodaSF###

class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'county', 'imageQ']
    
class SF_EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'venue', 'city', 'date']
    date_hierarchy= 'date'

class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'county', ]

class AgencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']

class OrgAdmin(admin.ModelAdmin):
    list_display = ['name', 'issue', 'category']

class PoliticianAdmin(admin.ModelAdmin):
    list_display = ['last_name','first_name', 'district', 'level', 'candidate',]
    
class BureaucratAdmin(admin.ModelAdmin):
    list_display = ['last_name','first_name', 'organization',]    

admin.site.register(County)
admin.site.register(Venue, VenueAdmin)
admin.site.register(Agency, AgencyAdmin)
admin.site.register(Genre)
admin.site.register(Issue)
admin.site.register(City, CityAdmin)
admin.site.register(Party)
admin.site.register(Level)
admin.site.register(SF_Event, SF_EventAdmin)
admin.site.register(Politician, PoliticianAdmin)
admin.site.register(Local_Link)
admin.site.register(District)
admin.site.register(Category)
admin.site.register(Organization, OrgAdmin)
admin.site.register(Bureaucrat, BureaucratAdmin)
admin.site.register(Program)
