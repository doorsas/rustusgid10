# Generated by Django 3.1.4 on 2021-03-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technikosnuoma', '0002_auto_20210304_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technika',
            name='nuotrauka',
            field=models.ImageField(blank=True, upload_to='technika/'),
        ),
    ]
