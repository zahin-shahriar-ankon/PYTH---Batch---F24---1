# Generated by Django 5.1 on 2024-09-28 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0002_intro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intro',
            old_name='a_name',
            new_name='i_name',
        ),
        migrations.RenameField(
            model_name='intro',
            old_name='a_occupation',
            new_name='i_occupation',
        ),
    ]
