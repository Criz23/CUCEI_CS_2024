# Generated by Django 2.2.13 on 2021-10-26 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0044_auto_20211026_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='isTrainingResource',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
