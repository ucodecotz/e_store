# Generated by Django 3.1.3 on 2020-11-14 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='mobile',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='tin',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]