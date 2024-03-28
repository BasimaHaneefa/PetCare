# Generated by Django 4.2.6 on 2023-12-27 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0004_tbl_hospital'),
        ('Admin', '0007_tbl_breedtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_rate', models.CharField(max_length=50)),
                ('product_photo', models.FileField(upload_to='ShopDoc/')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_shop')),
                ('subc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_subcategory')),
            ],
        ),
    ]