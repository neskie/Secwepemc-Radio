from django.conf.urls.defaults import *
from weblog.models import *

info_dict = {
    'queryset': Entry.objects.filter(status=1),
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
    (r'(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[-\w]+)/$', 'object_detail', dict(info_dict, slug_field='slug')),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$','archive_day',dict(info_dict)),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$','archive_month', dict(info_dict)),
    (r'^(?P<year>\d{4})/$','archive_year',
    dict(info_dict,make_object_list='True',allow_empty='True')),
    (r'^$','archive_index', dict(info_dict)),
)
