# Generated by Django 4.0.5 on 2022-06-20 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_alter_shop_background_image'),
        ('order', '0007_alter_orderitem_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.shop'),
        ),
    ]
