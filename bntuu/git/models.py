from django.db import models


class SaveFilesModell(models.Model):
    room_id = models.IntegerField()
    filee = models.FileField(upload_to='files/')
    time = models.CharField(max_length=16)
