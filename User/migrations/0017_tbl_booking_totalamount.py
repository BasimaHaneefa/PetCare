# Generated by Django 4.2.6 on 2024-01-09 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0016_alter_tbl_cart_food_alter_tbl_cart_pet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_booking',
            name='totalamount',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
