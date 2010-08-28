from django.conf.urls.defaults import *
from audio.models import *
from audio.feeds import LatestAudioFeed

info_dict = {
    'queryset': Audio.objects.all().order_by('-pub_date')
}

urlpatterns = patterns('',
    (r'^$','django.views.generic.list_detail.object_list',
        dict(info_dict,paginate_by=10)),
    (r'^detail/(?P<object_id>\d+)/$','django.views.generic.list_detail.object_detail', dict(info_dict)),
        (r'^latest/feed/$', LatestAudioFeed()),

)
