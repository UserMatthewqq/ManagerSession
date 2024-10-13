from django.db import models


class Save_P(models.Model):
    room_id = models.IntegerField()
    coordinates = models.CharField(max_length=50)
    text = models.TextField()


class SaveImageModel(models.Model):
    room_id = models.IntegerField()
    coordinates = models.CharField(max_length=50, null=True, blank=True)
    src = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
