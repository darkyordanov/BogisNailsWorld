# Generated by Django 5.0.1 on 2024-02-12 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_color_color_alter_naildesign_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naildesign',
            name='colors',
            field=models.CharField(choices=[('DARK', 'Dark'), ('LIGHT', 'Light'), ('RED', 'Red'), ('PINK', 'Pink'), ('BLUE', 'Blue'), ('PURPLE', 'Purple'), ('WHITE', 'White'), ('BLACK', 'Black'), ('GOLD', 'Gold'), ('NUDE', 'Nude'), ('YELLOW', 'Yellow'), ('ORANGE', 'Orange'), ('GREEN', 'Green'), ('BROWN', 'Brown'), ('GRAY', 'Gray')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Color',
        ),
    ]
