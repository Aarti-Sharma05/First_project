# Generated by Django 5.0.4 on 2024-05-20 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Blog Application', max_length=255),
        ),
    ]
