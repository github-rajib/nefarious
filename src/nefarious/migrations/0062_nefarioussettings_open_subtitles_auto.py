# Generated by Django 3.0.2 on 2021-03-16 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0061_auto_20210316_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='nefarioussettings',
            name='open_subtitles_auto',
            field=models.BooleanField(default=False, help_text='Whether to automatically download subtitles'),
        ),
    ]
