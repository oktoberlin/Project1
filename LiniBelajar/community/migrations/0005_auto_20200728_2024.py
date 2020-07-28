# Generated by Django 3.0.8 on 2020-07-28 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(default='default.jpg', upload_to='foto-post'),
        ),
    ]
