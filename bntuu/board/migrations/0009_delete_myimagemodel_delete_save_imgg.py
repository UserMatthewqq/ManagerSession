# Generated by Django 5.0.3 on 2024-05-14 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_saveimagemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyImageModel',
        ),
        migrations.DeleteModel(
            name='Save_Imgg',
        ),
    ]