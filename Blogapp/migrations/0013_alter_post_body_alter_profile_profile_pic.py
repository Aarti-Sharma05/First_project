# Generated by Django 5.0.4 on 2024-06-13 10:26

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogapp', '0012_profile_instagram_profile_facebook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='static/images/download.jpg', upload_to='images/profile/'),
        ),
    ]
