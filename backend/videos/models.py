from django.db import models
from django.conf import settings

# Create your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Video(TimeStampModel):
    title = models.CharField(max_length=30)
    thumbnail = models.ImageField()
    video_file = models.FileField(blank=False, null=False)
    tag_set = models.ManyToManyField('Tag', blank=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Tag(TimeStampModel):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name