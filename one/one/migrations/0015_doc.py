# Generated by Django 5.1 on 2024-09-28 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0014_dgvr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_description', models.CharField(max_length=100)),
            ],
        ),
    ]
