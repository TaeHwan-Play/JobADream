from django.db import models
from django.conf import settings

# Create your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Tag(TimeStampModel):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Board(TimeStampModel):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField()
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-id']