# Generated by Django 2.0.2 on 2018-04-11 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaperTraderApp', '0004_auto_20180409_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockmodel',
            name='symbol',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]