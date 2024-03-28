# Generated by Django 4.2.6 on 2024-01-14 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Petboarding', '0011_delete_tbl_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_photo', models.FileField(upload_to='BoardDoc/')),
                ('gallery_caption', models.CharField(max_length=60)),
                ('gd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Petboarding.tbl_gdetails')),
            ],
        ),
    ]
