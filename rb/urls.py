from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    (r'^genres/$','rb.views.genres'),
    (r'^artists/$','rb.views.artists'),
    (r'^albums/$','rb.views.albums'),
    (r'^player/play/$','rb.views.play'),
    (r'^player/next/$','rb.views.next'),
    (r'^player/pause/$','rb.views.pause'),
    (r'^artists/(?P<slug>[\w\W]+)/$' ,'rb.views.artists_detail'),
    (r'^albums/(?P<slug>[\w\W]+)/$' ,'rb.views.album_detail'),
    (r'^player/$', login_required(direct_to_template),
        {'template': 'rb/player.html'}),
)

