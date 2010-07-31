from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^genres/$','rb.views.genres'),
    (r'^artists/$','rb.views.artists'),
    (r'^albums/$','rb.views.albums'),
    (r'^artists/(?P<slug>[\w\W]+)/$' ,'rb.views.artists_detail'),
    (r'^albums/(?P<slug>[\w\W]+)/$' ,'rb.views.album_detail'),
)

