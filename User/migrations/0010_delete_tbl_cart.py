# Generated by Django 4.2.6 on 2024-01-06 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_alter_tbl_cart_food_alter_tbl_cart_pet_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_cart',
        ),
    ]
