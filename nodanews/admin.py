from django.contrib import admin
from .models import Event, Front_Page, Variation, Theme, Category, Author, Other_Link, Report_Link, Media_Org, Blog, Node, Media_Org, Link, Perspective, Node_Dir, Region, Journalist, Political_Lean, Media_Character, About, Topic_Link, PoliticalBiasNews, Blog, Analysis, AnalLink, AnalPerspective, PoliticalIssue, STF, STF_Hub, STF_Link, Feature, Feature_Link 

class EventAdmin(admin.ModelAdmin):
    list_display = ['headline', 'theme']

class Other_LinkAdmin(admin.ModelAdmin):
    list_display = ['category', 'media', 'posted',]
    
class Report_LinkAdmin(admin.ModelAdmin):
    list_display = ['media', 'event', 'title']

admin.site.register(Category)
admin.site.register(Front_Page)
admin.site.register(Variation)
admin.site.register(Author)
admin.site.register(Event, EventAdmin)
admin.site.register(Theme)
admin.site.register(Media_Org)
admin.site.register(Blog)
admin.site.register(Report_Link, Report_LinkAdmin)
admin.site.register(About)
admin.site.register(Other_Link, Other_LinkAdmin)


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
