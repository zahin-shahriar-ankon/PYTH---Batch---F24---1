# Generated by Django 5.1 on 2024-09-28 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0011_thddeg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pjct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pjct_description', models.CharField(max_length=100)),
            ],
        ),
    ]
