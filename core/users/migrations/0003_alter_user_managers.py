# Generated by Django 4.2.11 on 2024-03-21 08:18

from django.db import migrations

import users.managers
import users.models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_remove_user_username"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", users.managers.CustomUserManager()),
            ],
        ),
    ]
