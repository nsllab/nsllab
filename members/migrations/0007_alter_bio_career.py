# Generated by Django 4.2.9 on 2024-01-10 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_bio_display_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='career',
            field=models.TextField(blank=True, null=True),
        ),
    ]
