from django.db import models
import mimetypes
from radio.settings import MEDIA_ROOT
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import datetime

# Create your models here.
class Audio(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    audiofile = models.FileField(upload_to='files/audio/')
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    def mimetype(self):
        return mimetypes.guess_type("%s%s"%(MEDIA_ROOT,self.audiofile))[0]
    def metadata(self):
        filename = "%s%s"%(MEDIA_ROOT,self.audiofile)
        return MP3(filename,ID3=EasyID3)
