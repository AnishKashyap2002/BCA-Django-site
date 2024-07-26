# Generated by Django 4.1.7 on 2023-03-11 11:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_remove_user_following_user_followings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='user',
            name='followings',
        ),
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
