# Generated by Django 3.0.2 on 2020-09-24 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ott', '0007_auto_20200924_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='banner_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_image1', models.ImageField(blank=True, null=True, upload_to='')),
                ('banner_image1_link', models.CharField(max_length=3000)),
                ('banner_image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('banner_image2_link', models.CharField(max_length=3000)),
                ('banner_image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('banner_image3_link', models.CharField(max_length=3000)),
            ],
        ),
    ]
