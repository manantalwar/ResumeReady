# Generated by Django 3.2.14 on 2024-05-07 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10, verbose_name='Phone')),
                ('linkedin', models.URLField(verbose_name='LinkedIn')),
                ('website', models.URLField(verbose_name='Website')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=30, verbose_name='Degree')),
                ('major', models.CharField(max_length=30, verbose_name='Major')),
                ('institution', models.CharField(max_length=30, verbose_name='Institution')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('coursework', models.TextField(blank=True)),
                ('gpa', models.FloatField(verbose_name='GPA')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=30, verbose_name='Role')),
                ('company', models.CharField(max_length=30, verbose_name='Company')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ResumeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='details.contact')),
                ('education', models.ManyToManyField(blank=True, null=True, to='details.Education')),
                ('experiences', models.ManyToManyField(blank=True, null=True, to='details.Experience')),
                ('skillset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='details.skills')),
            ],
        ),
    ]
