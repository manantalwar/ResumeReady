# Generated by Django 3.2.14 on 2024-05-12 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0006_auto_20240509_0459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('owner', models.IntegerField(default=1, verbose_name='Job Owner')),
            ],
        ),
    ]
