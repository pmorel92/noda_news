# Generated by Django 3.0.6 on 2020-05-08 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0018_front_page_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='body',
            field=models.TextField(blank=True, default=' '),
        ),
        migrations.AlterField(
            model_name='event',
            name='body2',
            field=models.TextField(blank=True, default=' '),
        ),
        migrations.AlterField(
            model_name='event',
            name='credit1',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='credit2',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='headline',
            field=models.CharField(blank=True, default=' ', max_length=150),
        ),
        migrations.AlterField(
            model_name='event',
            name='image1',
            field=models.ImageField(blank=True, default='', upload_to='media/stock'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image2',
            field=models.ImageField(blank=True, default='', upload_to='media/stock'),
        ),
        migrations.AlterField(
            model_name='event',
            name='lead',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='theme',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='nodanews.Theme'),
        ),
    ]