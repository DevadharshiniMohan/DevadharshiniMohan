# Generated by Django 4.1.5 on 2023-01-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0023_alter_office_staff_skills"),
    ]

    operations = [
        migrations.AlterField(
            model_name="office_staff",
            name="ID",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]