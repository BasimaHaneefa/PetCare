# Generated by Django 4.2.6 on 2023-12-23 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_tbl_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_breedtype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed_name', models.CharField(max_length=50)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_subcategory')),
            ],
        ),
    ]