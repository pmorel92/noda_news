# Generated by Django 3.0.2 on 2020-02-25 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0011_auto_20200225_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='credit',
            field=models.CharField(default=' ', max_length=150),
        ),
        migrations.AddField(
            model_name='sequence',
            name='credit',
            field=models.CharField(default=' ', max_length=150),
        ),
    ]
