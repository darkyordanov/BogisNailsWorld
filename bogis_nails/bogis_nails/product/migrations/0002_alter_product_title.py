# Generated by Django 5.0.1 on 2024-03-03 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=36, null=True),
        ),
    ]