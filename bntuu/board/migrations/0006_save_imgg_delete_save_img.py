# Generated by Django 5.0.3 on 2024-05-06 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_save_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Save_Imgg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('coordinates', models.CharField(max_length=50)),
                ('filename', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Save_Img',
        ),
    ]