# Generated by Django 4.2.2 on 2023-06-17 20:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="address",
            old_name="user_id",
            new_name="user",
        ),
    ]
