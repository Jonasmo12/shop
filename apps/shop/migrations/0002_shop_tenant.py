# Generated by Django 4.0.5 on 2022-06-07 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='tenant',
            field=models.TextField(default='shared', verbose_name='tenant'),
        ),
    ]
