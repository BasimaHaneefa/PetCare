# Generated by Django 4.2.6 on 2024-01-06 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_tbl_pet'),
        ('User', '0007_tbl_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_qty', models.CharField(max_length=50)),
                ('cart_status', models.CharField(default=0, max_length=2)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_booking')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.tbl_food')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.tbl_pet')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.tbl_product')),
            ],
        ),
    ]
