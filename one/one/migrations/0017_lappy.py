# Generated by Django 5.1 on 2024-09-28 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0016_face'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lappy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face_description', models.CharField(max_length=100)),
            ],
        ),
    ]