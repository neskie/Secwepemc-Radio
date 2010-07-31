import sys
from show.models import *
f = open('shows.csv')

shows = {}

line = f.readline()
while line:
    a = line.strip().split('\t')[:-1]
    shows[a[0]] = a[1:]
    line = f.readline()

for hour in range(7,24):
    for day,show in enumerate( shows[str(hour)]):
        try:
            slot = Slot(dayofweek=day+1,hour=hour,show=Show.objects.get(title=show))
            slot.save()
        except:
            print show
