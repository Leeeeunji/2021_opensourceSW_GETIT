# Generated by Django 3.2.6 on 2021-08-23 22:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_mentor_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='PUBLISH DATE'),
        ),
    ]