# Generated by Django 4.0.5 on 2022-06-19 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_rename_full_name_order_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]
