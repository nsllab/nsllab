# Generated by Django 4.2.9 on 2024-01-15 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0003_remove_weeklyreport_writer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weeklyreport',
            old_name='paper_last_week',
            new_name='paper_last_wk',
        ),
        migrations.RenameField(
            model_name='weeklyreport',
            old_name='paper_this_week',
            new_name='paper_this_wk',
        ),
        migrations.RenameField(
            model_name='weeklyreport',
            old_name='project_last_week',
            new_name='project_last_wk',
        ),
        migrations.RenameField(
            model_name='weeklyreport',
            old_name='project_this_week',
            new_name='project_this_wk',
        ),
    ]
