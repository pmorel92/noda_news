# Generated by Django 3.0.2 on 2020-05-07 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0017_auto_20200506_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='front_page',
            name='title',
            field=models.CharField(default='date written out', max_length=100),
        ),
    ]