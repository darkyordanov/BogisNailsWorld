# Generated by Django 5.0.1 on 2024-03-15 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_remove_profile_birth_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
