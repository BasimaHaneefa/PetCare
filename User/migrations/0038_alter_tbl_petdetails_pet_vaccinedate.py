# Generated by Django 4.2.6 on 2024-03-23 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0037_alter_tbl_petdetails_pet_vaccinedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_petdetails',
            name='pet_vaccinedate',
            field=models.DateField(max_length=20, null=True),
        ),
    ]