# Generated by Django 4.2.9 on 2024-01-15 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0004_rename_paper_last_week_weeklyreport_paper_last_wk_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weeklyreport',
            old_name='paper_prog_percen',
            new_name='paper_prog_percent',
        ),
        migrations.RenameField(
            model_name='weeklyreport',
            old_name='project_prog_percen',
            new_name='project_prog_percent',
        ),
    ]
