# Generated by Django 5.1 on 2024-10-16 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0011_experiences'),
    ]

    operations = [
        migrations.CreateModel(
            name='AExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_ex_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.RenameModel(
            old_name='Experiences',
            new_name='Experience',
        ),
    ]
