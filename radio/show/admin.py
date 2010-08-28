from django.contrib import admin
from radio.show.models import *

class SlotInline(admin.TabularInline):
    model = Slot

class ShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'host', 'slots','count')
    search_fields = ('title', 'host')
    list_filter = ('host','title',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        SlotInline,
    ]
class SlotAdmin(admin.ModelAdmin):
    list_display = ('dayofweek','hour','show', )
    list_filter = ('dayofweek', 'hour',)

admin.site.register(Show,ShowAdmin)
admin.site.register(Slot,SlotAdmin)
