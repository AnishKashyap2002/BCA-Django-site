# Generated by Django 4.1.7 on 2023-03-10 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_comment_post_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment_post',
            old_name='users',
            new_name='user',
        ),
    ]
