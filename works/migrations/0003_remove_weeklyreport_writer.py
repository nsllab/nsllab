# Generated by Django 4.2.9 on 2024-01-15 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_alter_weeklyreport_fr_dt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weeklyreport',
            name='writer',
        ),
    ]
