# Generated by Django 4.2.9 on 2024-01-16 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0012_alter_patent_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patent',
            name='patent_type',
            field=models.IntegerField(choices=[(1, 'International'), (2, 'Domestic')], default=1, null=True),
        ),
    ]
