# Generated by Django 4.2.6 on 2024-01-29 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0021_tbl_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_petdetails',
            name='pet_vaccinedate',
            field=models.DateField(max_length=20),
        ),
    ]
