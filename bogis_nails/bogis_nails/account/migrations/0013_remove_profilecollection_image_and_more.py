# Generated by Django 5.0.1 on 2024-03-25 21:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_image_alter_profile_user_profilecollection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilecollection',
            name='image',
        ),
        migrations.RemoveField(
            model_name='profilecollection',
            name='user',
        ),
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='ProfileCollection',
        ),
    ]
