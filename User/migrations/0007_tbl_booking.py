# Generated by Django 4.2.6 on 2024-01-06 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_tbl_hospital'),
        ('User', '0006_tbl_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('booking_status', models.CharField(default=0, max_length=2)),
                ('payment_status', models.CharField(default=0, max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
