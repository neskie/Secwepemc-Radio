from django.contrib.gis import admin
from models import *

admin.site.register(NationBorders, admin.OSMGeoAdmin)
