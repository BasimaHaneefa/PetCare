# Generated by Django 4.2.6 on 2023-12-28 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_tbl_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_complaint',
            name='complaint_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
