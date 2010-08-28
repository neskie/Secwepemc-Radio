# Create your views here.
from django.views.generic.list_detail import object_list
from show.models import *
from django.core import serializers
from django.http import HttpResponse
import json
 
def show_by_day(request, dayofweek):
    show_list = Slot.objects.filter(dayofweek=0)

    choices = []
    for dow in Slot.DOW_CHOICES:
        choices.append(dow[1])
        if dayofweek == dow[1]:
            show_list = Slot.objects.filter(dayofweek=dow[0])

    context = { 'dayofweek': dayofweek,
            'choices':choices, 
            }
    return object_list(request,
            queryset=show_list,template_name='show/slot_day.html',extra_context=context)

def json_schedule(request):
    json = serializers.serialize("json", Slot.objects.all())
    return HttpResponse(json, mimetype='application/json')

def json_shows(request):
    json = serializers.serialize("json", Show.objects.all())
    json = json[:-1]+', '+serializers.serialize("json", Slot.objects.all())[1:]
    return HttpResponse(json, mimetype='application/json')

def json_show(request,hour,dayofweek):
    slot = Slot.objects.get(hour=hour,dayofweek=dayofweek)
    show = slot.show

    data = [slot, show]
    json_data = serializers.serialize("json", data )
    return HttpResponse(json_data, mimetype='application/json')
