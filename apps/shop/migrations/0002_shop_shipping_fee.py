# Generated by Django 4.0.5 on 2022-08-14 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shipping_fee',
            field=models.FloatField(null=True),
        ),
    ]