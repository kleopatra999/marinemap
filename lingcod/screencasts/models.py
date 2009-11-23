from django.contrib.gis.db import models
from django.conf import settings

class Screencast(models.Model):
    video = models.FileField(upload_to=settings.SCREENCASTS)
    image = models.ImageField(upload_to=settings.SCREENCAST_IMAGES)
    title = models.CharField(max_length=100)
    urlname = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    
    class Meta:
        db_table = 'mm_screencast'
        
    def __unicode__(self):
        return self.title

    