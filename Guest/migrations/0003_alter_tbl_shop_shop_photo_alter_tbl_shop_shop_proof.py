# Generated by Django 4.2.6 on 2023-12-21 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0002_tbl_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_shop',
            name='shop_photo',
            field=models.FileField(upload_to='ShopDoc/'),
        ),
        migrations.AlterField(
            model_name='tbl_shop',
            name='shop_proof',
            field=models.FileField(upload_to='ShopDoc/'),
        ),
    ]
