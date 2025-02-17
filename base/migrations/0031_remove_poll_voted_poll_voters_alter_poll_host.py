# Generated by Django 4.1.7 on 2023-03-21 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_poll_voted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='voted',
        ),
        migrations.AddField(
            model_name='poll',
            name='voters',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='poll',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='polls', to=settings.AUTH_USER_MODEL),
        ),
    ]
