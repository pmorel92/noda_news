from django.contrib import admin
from .models import Event, Theme, Report_Link, Media_Org, Blog, Node, Media_Org, Link, Perspective, Node_Dir, Region, Journalist, Political_Lean, Media_Character, About, Topic_Link, PoliticalBiasNews, Blog, Analysis, AnalLink, AnalPerspective, PoliticalIssue, STF, STF_Hub, STF_Link, Feature, Feature_Link, County, Venue, Agency, Genre, Issue, City, Party, Level, SF_Event, Politician, Local_Link, District, Category, Organization, Program, Bureaucrat



admin.site.register(Event)
admin.site.register(Theme)
admin.site.register(Media_Org)
admin.site.register(Blog)
admin.site.register(Report_Link)
admin.site.register(About)

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
####Archives###
    

#admin.site.register(Node)
#admin.site.register(Node_Dir)
#admin.site.register(Region)
#admin.site.register(Link)
#admin.site.register(Perspective)
#admin.site.register(Political_Lean)

#admin.site.register(Topic_Link)
#admin.site.register(Media_Character)
#admin.site.register(Journalist)
#admin.site.register(PoliticalBiasNews)
#admin.site.register(Analysis)
#admin.site.register(AnalLink)
#admin.site.register(AnalPerspective)
#admin.site.register(PoliticalIssue)
#admin.site.register(STF)
#admin.site.register(STF_Link)
#admin.site.register(STF_Hub)
#admin.site.register(Feature)
#admin.site.register(Feature_Link)
