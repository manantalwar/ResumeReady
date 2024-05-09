# Generated by Django 3.2.14 on 2024-05-09 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_auto_20240509_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='owner',
            field=models.IntegerField(default=1, verbose_name='Education Owner'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='owner',
            field=models.IntegerField(default=1, verbose_name='Experience Owner'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='owner',
            field=models.IntegerField(default=1, verbose_name='Skills Owner'),
        ),
    ]
