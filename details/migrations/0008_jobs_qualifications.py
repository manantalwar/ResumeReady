# Generated by Django 3.2.14 on 2024-05-12 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0007_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='qualifications',
            field=models.TextField(blank=True),
        ),
    ]
