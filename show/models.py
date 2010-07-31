from django.db import models
import datetime
from django.db import models
from django.contrib.auth.models import User

class Show(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    host = models.ForeignKey(User)
    url = models.URLField(blank=True)
#    description = models.CharField(max_length=1000)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    syndicated = models.BooleanField(default=False)
 
    class Meta:
        verbose_name_plural = "Shows"
    def __unicode__(self):
        return self.title
    def slots(self):
        string = ''
        for slot in self.slot_set.all():
            string += "|%s"%slot
        return string
    def count (self):
        return self.slot_set.count()
    def get_absolute_url(self):
        return "/show/detail/%s" % self.slug
 
class Slot(models.Model):
    SUN = 1
    MON = 2
    TUE = 3
    WED = 4
    THU = 5
    FRI = 6
    SAT = 7
    DOW_CHOICES = ((SUN, 'Sunday'),
        (MON, 'Monday'),
        (TUE, 'Tuesday'),
        (WED, 'Wednesday'),
        (THU, 'Thursday'),
        (FRI, 'Friday'),
        (SAT, 'Saturday'))

    dayofweek = models.IntegerField(choices=DOW_CHOICES, default=SUN)

    HOUR_CHOICES = ((7,'7 am'),
            (8, '8 am'),
            (9, '9 am'),
            (10, '10 am'),
            (11, '11 am'),
            (12, '12 pm'),
            (13, '1 pm'),
            (14, '2 pm'),
            (15, '3 pm'),
            (16, '4 pm'),
            (17, '5 pm'),
            (18, '6 pm'),
            (19, '7 pm'),
            (20, '8 pm'),
            (21, '9 pm'),
            (22, '10 pm'),
            (23, '11 pm'),
            (24, '12 am'),
        )

    hour = models.IntegerField(choices=HOUR_CHOICES)
    show = models.ForeignKey(Show)
    class Meta:
        ordering = ['dayofweek', 'hour']
        unique_together = (("dayofweek", "hour"),)
    def __unicode__(self):
        return "%s on %s"%(self.get_hour_display(),self.get_dayofweek_display())
