# Generated by Django 2.2.28 on 2023-04-02 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0065_auto_20230402_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='day',
        ),
    ]
