import datetime
from django.db import models
from django.contrib.auth.models import User
 
class Entry(models.Model):
    title = models.CharField(max_length=250)
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField()
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
 
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = ((LIVE_STATUS, 'Live'),
              (DRAFT_STATUS, 'Draft'),
              (HIDDEN_STATUS, 'Hidden'))
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
 
    class Meta:
        verbose_name_plural = "Entries"
        ordering = ('-pub_date', )
 
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return "/weblog/%s" % (self.slug)
