from django.contrib.syndication.views import Feed
from audio.models import *
from django.conf import settings
class LatestAudioFeed(Feed):
    title = "Secwepemc Radio Audio"
    link = "/audio/"
    description = "Updates Audiofiles that have been uploaded to the site."

    def items(self):
        return Audio.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.metadata

    def item_link(self, item):
        return str(item.audiofile)
