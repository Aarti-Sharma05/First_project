# Generated by Django 5.0.4 on 2024-07-04 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogapp', '0014_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='/static/images/download.jpg', upload_to='images/profile/'),
        ),
    ]
