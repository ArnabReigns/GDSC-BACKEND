from django.db import models

# Create your models here.

class GDSC_Gallery(models.Model):
    thumbnail = models.ImageField(upload_to="media/gallery/")
    caption = models.CharField(max_length=1000)
    description = models.TextField(blank=True,null=True)