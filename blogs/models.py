from django.db import models

# Create your models here.

class Blog(models.Model):
    caption = models.CharField(max_length=4000)
    image = models.ImageField(upload_to="media/blogs/")
    description = models.TextField()
    link = models.URLField()
    