# Generated by Django 4.2.6 on 2024-01-29 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0005_tbl_petboarding'),
        ('User', '0022_alter_tbl_petdetails_pet_vaccinedate'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_rating', models.IntegerField(max_length=20)),
                ('user_review', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('review_datetime', models.DateTimeField(auto_now_add=True)),
                ('petboarding', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_petboarding')),
                ('shop', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_shop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
