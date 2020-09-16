# Generated by Django 3.0.2 on 2020-09-16 13:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ott', '0002_movies_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, related_name='bookmarks', to=settings.AUTH_USER_MODEL),
        ),
    ]
