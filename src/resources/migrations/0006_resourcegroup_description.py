# Generated by Django 2.2.9 on 2020-01-28 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20200128_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcegroup',
            name='description',
            field=models.CharField(default='description', max_length=200),
            preserve_default=False,
        ),
    ]
