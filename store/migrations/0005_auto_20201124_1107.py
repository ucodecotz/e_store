# Generated by Django 3.1.3 on 2020-11-24 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
