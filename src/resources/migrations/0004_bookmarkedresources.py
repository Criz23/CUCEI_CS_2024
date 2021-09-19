# Generated by Django 2.2.13 on 2021-09-13 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resources', '0003_auto_20210809_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookmarkedResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Resource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'resource')},
            },
        ),
    ]
