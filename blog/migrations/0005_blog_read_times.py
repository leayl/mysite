# Generated by Django 2.0 on 2019-04-24 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190424_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='read_times',
            field=models.IntegerField(default=0),
        ),
    ]
