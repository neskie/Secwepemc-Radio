from django.conf.urls.defaults import *
from show.models import *

info_dict = {
    'queryset': Slot.objects.all().order_by('hour','dayofweek'),
}

show_dict = {
    'queryset': Show.objects.all(),
}

urlpatterns = patterns('',
    (r'^$','django.views.generic.list_detail.object_list',
        dict(info_dict, extra_context={'dayofweek':Slot.DOW_CHOICES} )),
    (r'^browse/day/(?P<dayofweek>\w+)/$','show.views.show_by_day'),
    (r'^schedule/json/$','show.views.json_schedule'),
    (r'^shows/json/$','show.views.json_shows'),
    (r'^detail/(?P<slug>[\w-]+)/$','django.views.generic.list_detail.object_detail', dict(show_dict,slug_field='slug')),
    (r'^json/(?P<hour>\d+)/(?P<dayofweek>\d+)/$','show.views.json_show'),
)

