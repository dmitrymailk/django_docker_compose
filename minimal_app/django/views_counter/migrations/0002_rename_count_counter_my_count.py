# Generated by Django 4.0.7 on 2022-08-28 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('views_counter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='counter',
            old_name='count',
            new_name='my_count',
        ),
    ]