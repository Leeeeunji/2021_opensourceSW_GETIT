# Generated by Django 3.2.6 on 2021-08-23 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_mentor_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mentor',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Mentors', 'verbose_name_plural': 'Mentors'},
        ),
        migrations.AlterField(
            model_name='mentor',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='PUBLISH DATE'),
        ),
    ]