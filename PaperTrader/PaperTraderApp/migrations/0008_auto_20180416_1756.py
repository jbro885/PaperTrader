# Generated by Django 2.0.2 on 2018-04-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaperTraderApp', '0007_auto_20180415_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockmodel',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='stockmodel',
            name='symbol',
            field=models.CharField(max_length=6),
        ),
    ]