# Generated by Django 2.1.1 on 2018-12-08 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0009_auto_20181207_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nefarioussettings',
            old_name='quality_profile',
            new_name='quality_profile_movies',
        ),
        migrations.AddField(
            model_name='nefarioussettings',
            name='quality_profile_tv',
            field=models.CharField(choices=[('any', 'any'), ('sd', 'sd'), ('hd-720p', 'hd-720p'), ('hd-720p-1080p', 'hd-720p-1080p'), ('hd-1080p', 'hd-1080p'), ('ultra-hd', 'ultra-hd')], default='hd-720p-1080p', max_length=500),
        ),
        migrations.AlterField(
            model_name='nefarioussettings',
            name='tmdb_token',
            field=models.CharField(default='21c8985a267ac3f11ea75baf2c05c3ba', max_length=500),
        ),
    ]
