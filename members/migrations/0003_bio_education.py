# Generated by Django 4.2.9 on 2024-01-10 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio',
            name='education',
            field=models.TextField(default='Seoul university, KIT'),
            preserve_default=False,
        ),
    ]
