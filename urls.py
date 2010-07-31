from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.sitemaps import Sitemap
from show.models import Show

class ShowSiteMap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Show.objects.all()
    def location(self):
        return "/show/"

sitemaps = { 'shows': ShowSiteMap }

urlpatterns = patterns('',
    # Example:
    (r'^weblog/', include('weblog.urls')),
    (r'^show/', include('show.urls')),
    (r'^audio/', include('audio.urls')),
    (r'^rb/', include('rb.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page':'/'}),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})



)
