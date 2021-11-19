# Generated by Django 3.2.9 on 2021-11-18 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20211118_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='extraction_method',
            field=models.CharField(blank=True, choices=[('soxhlet', 'Soxhlet'), ('saponification', 'Saponification'), ('sepratory funnel', 'Sepratory Funnel'), ('roller', 'Roller'), ('other', 'Other')], max_length=100),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='sample_type',
            field=models.CharField(blank=True, choices=[('wet sediment', 'Wet Sediment'), ('dry sediment', 'Dry Sediment'), ('water', 'Water'), ('water & solvent', 'Water & Solvent'), ('extract', 'Extract')], max_length=100),
        ),
    ]
