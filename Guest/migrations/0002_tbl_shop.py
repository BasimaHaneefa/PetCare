# Generated by Django 4.2.6 on 2023-12-21 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_tbl_admin'),
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=50)),
                ('shop_address', models.CharField(max_length=50)),
                ('shop_contact', models.CharField(max_length=15)),
                ('shop_email', models.CharField(max_length=50)),
                ('shop_password', models.CharField(max_length=8)),
                ('shop_photo', models.FileField(upload_to='ShopPhoto/')),
                ('shop_proof', models.FileField(upload_to='ShopPhoto/')),
                ('shop_vstatus', models.CharField(default=0, max_length=2)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
