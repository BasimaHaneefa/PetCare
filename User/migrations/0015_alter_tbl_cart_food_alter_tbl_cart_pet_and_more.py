# Generated by Django 4.2.6 on 2024-01-06 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_tbl_pet'),
        ('User', '0014_tbl_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_cart',
            name='food',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.tbl_food'),
        ),
        migrations.AlterField(
            model_name='tbl_cart',
            name='pet',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.tbl_pet'),
        ),
        migrations.AlterField(
            model_name='tbl_cart',
            name='product',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop.tbl_product'),
        ),
    ]