from django.contrib import admin
from models import *

#class CapchaAdmin(admin.ModelAdmin):
#    list_display = ('ip',  'capcha')

class OfertaAdmin(admin.ModelAdmin):
    list_display = ('ip',  'date','firma','email','area','title')

class CVAdmin(admin.ModelAdmin):
    list_display = ('ip',  'date','title','area','email')


#admin.site.register(Capcha,CapchaAdmin)
admin.site.register(Oferta,OfertaAdmin)
admin.site.register(CV, CVAdmin)