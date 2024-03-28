# Generated by Django 4.2.6 on 2023-12-26 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0004_tbl_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_petdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_dob', models.CharField(max_length=50)),
                ('breedtype_name', models.CharField(max_length=50)),
                ('pet_weight', models.CharField(max_length=50)),
                ('pet_vaccinedate', models.CharField(max_length=20)),
                ('pet_details', models.CharField(max_length=100)),
                ('pet_vaccinename', models.CharField(max_length=50)),
                ('pet_photo', models.FileField(upload_to='UserPhoto/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
