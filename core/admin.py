from django.contrib import admin

# Register your models here.
from core.models import Etat,Profil,Photo

admin.site.register([Etat,Photo])

class PhotoInline(admin.TabularInline):
    model = Photo

class ProfilAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline
    ]
admin.site.register(Profil,ProfilAdmin)
