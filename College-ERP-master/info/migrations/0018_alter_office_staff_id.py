# Generated by Django 4.1.5 on 2023-01-09 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0017_office_staff_alter_user_first_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="office_staff",
            name="ID",
            field=models.UUIDField(
                auto_created=True, primary_key=True, serialize=False, unique=True
            ),
        ),
    ]
