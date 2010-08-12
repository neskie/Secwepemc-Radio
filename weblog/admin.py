from django.contrib import admin
from tagging.models import *
from radio.weblog.models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = ('author','pub_date','title', 'status')
    search_fields = ('title', 'post')
    list_filter = ('author', 'pub_date')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Entry,EntryAdmin)
