# Generated by Django 3.0.8 on 2020-07-28 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_remove_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='foto-post'),
        ),
    ]
