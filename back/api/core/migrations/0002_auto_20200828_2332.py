# Generated by Django 3.1 on 2020-08-28 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='url',
            new_name='slug',
        ),
    ]
