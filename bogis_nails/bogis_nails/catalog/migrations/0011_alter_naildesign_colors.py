# Generated by Django 5.0.1 on 2024-02-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_naildesign_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naildesign',
            name='colors',
            field=models.CharField(choices=[('DARK', 'Dark'), ('LIGHT', 'Light'), ('RED', 'Red'), ('PINK', 'Pink'), ('BLUE', 'Blue'), ('PURPLE', 'Purple'), ('WHITE', 'White'), ('BLACK', 'Black'), ('GOLD', 'Gold'), ('YELLOW', 'Yellow'), ('ORANGE', 'Orange'), ('GREEN', 'Green'), ('BROWN', 'Brown'), ('GRAY', 'Gray')], default='DARK', max_length=20),
        ),
    ]
