# Generated by Django 3.1.4 on 2021-02-15 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='nu cia tai sakes', max_length=255),
        ),
    ]
