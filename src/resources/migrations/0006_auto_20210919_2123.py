# Generated by Django 2.2.13 on 2021-09-19 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20210919_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='learningResourceType',
        ),
        migrations.AddField(
            model_name='resource',
            name='learningResourceType',
            field=models.ManyToManyField(to='resources.LearningResourceType'),
        ),
    ]
