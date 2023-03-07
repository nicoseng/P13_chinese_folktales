from django.contrib.auth.models import User
from django.db import models


class Level(models.Model):
    class Meta:
        ordering = ['level_id']

    level_id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=500, null=True)


class Story(models.Model):

    class Meta:
        ordering = ['story_id']

    story_id = models.IntegerField(primary_key=True)
    level_id = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    title = models.fields.TextField(max_length=1000, null=True)
    chinese_title = models.fields.TextField(max_length=1000, null=True)
    bg_image = models.URLField(max_length=1000)
    textfile = models.fields.TextField(max_length=1000, null=True)
    audiofile = models.URLField(max_length=1000)
    audio_bg_image = models.URLField(max_length=1000, null=True)
    description = models.fields.TextField(max_length=1000, null=True)
    date = models.DateTimeField(auto_now_add=True)


class Favorite(models.Model):
    class Meta:
        ordering = ['story_id']

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    story_id = models.ForeignKey(Story, on_delete=models.CASCADE, null=True)
