# Generated by Django 2.2.10 on 2020-03-29 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default_blog.png', max_length=200, upload_to=''),
        ),
    ]
