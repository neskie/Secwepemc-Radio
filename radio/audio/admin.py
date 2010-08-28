from audio.models import *
from django.contrib import admin
class AudioAdmin(admin.ModelAdmin):
    list_display = ('name','audiofile', )

admin.site.register(Audio,AudioAdmin)
