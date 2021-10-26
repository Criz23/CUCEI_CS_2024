# Generated by Django 2.2.10 on 2020-03-04 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('resources', '0016_auto_20200304_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resource',
            name='author_rsc',
        ),
        migrations.AddField(
            model_name='resource',
            name='author_rsc',
            field=models.ManyToManyField(to='authors.Author'),
        ),
    ]
