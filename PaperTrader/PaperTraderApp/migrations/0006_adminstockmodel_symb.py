# Generated by Django 2.0.2 on 2018-04-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaperTraderApp', '0005_auto_20180411_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminstockmodel',
            name='symb',
            field=models.CharField(default='null', max_length=60),
            preserve_default=False,
        ),
    ]
