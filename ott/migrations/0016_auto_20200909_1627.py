# Generated by Django 3.0.2 on 2020-09-09 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ott', '0015_auto_20200909_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ott.Languages'),
        ),
    ]