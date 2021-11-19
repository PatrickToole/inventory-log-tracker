# Generated by Django 3.2.9 on 2021-11-19 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20211118_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='sample_cleanup',
            field=models.CharField(blank=True, choices=[('silica gel', 'Silica Gel'), ('gpc', 'GPC'), ('purge & trap', 'Purge & Trap'), ('none', 'None')], max_length=100),
        ),
    ]
