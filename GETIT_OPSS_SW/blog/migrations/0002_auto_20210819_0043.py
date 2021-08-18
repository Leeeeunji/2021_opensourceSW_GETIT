# Generated by Django 3.2.6 on 2021-08-18 15:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='mentor',
            name='recruit_center',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='recruit_endDate',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='recruit_number',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='mentor',
            name='recruit_startdate',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='volun_day',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='volun_endDate',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='volun_for',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='volun_place',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='volun_startDate',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='volun_times',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mentor',
            name='volun_type',
            field=models.TextField(blank=True),
        ),
    ]