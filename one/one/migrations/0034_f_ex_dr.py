# Generated by Django 5.1 on 2024-09-29 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0033_f_rch_dr'),
    ]

    operations = [
        migrations.CreateModel(
            name='F_ex_dr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_ex_dr', models.CharField(max_length=100)),
            ],
        ),
    ]