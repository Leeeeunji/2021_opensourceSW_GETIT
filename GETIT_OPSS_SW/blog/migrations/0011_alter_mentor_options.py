# Generated by Django 3.2.6 on 2021-08-23 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_mentor_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mentor',
            options={'ordering': ('-pub_date',), 'verbose_name': 'Mentor', 'verbose_name_plural': 'Mentors'},
        ),
    ]