# Generated by Django 4.1.5 on 2023-01-11 04:59

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0030_alter_office_staff_designation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="office_staff",
            name="Skills",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    (
                        "Critical thinking and problem solving",
                        "Critical thinking and problem solving",
                    ),
                    (
                        "Professionalism and strong work ethic",
                        "Professionalism and strong work ethic",
                    ),
                    (
                        "Oral and written communications skills",
                        "Oral and written communications skills",
                    ),
                ],
                max_length=100,
            ),
        ),
    ]