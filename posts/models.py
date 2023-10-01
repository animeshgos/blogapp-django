from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Post(models.Model):
    tag = models.ForeignKey(
        Tag, related_name='posts', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
