# Generated by Django 3.2.6 on 2021-08-22 07:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentee',
            name='mentoringEnd_times',
        ),
        migrations.RemoveField(
            model_name='mentee',
            name='mentoringStart_times',
        ),
        migrations.AddField(
            model_name='mentee',
            name='study_times',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='mentee',
            name='mentoringType',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mentee',
            name='partMentor',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='recruit_endDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='recruit_startdate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='volun_endDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='volun_startDate',
            field=models.DateField(blank=True),
        ),
    ]
