# Generated by Django 3.0.8 on 2020-07-17 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default3.jpg', upload_to='foto-profil'),
        ),
    ]