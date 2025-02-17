# Generated by Django 4.1.7 on 2023-03-10 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_post_likes_delete_post_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.post')),
                ('users', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
