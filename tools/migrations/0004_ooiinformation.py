# Generated by Django 3.2.4 on 2021-08-03 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tools", "0003_change_orgazation_host_to_code"),
    ]

    operations = [
        migrations.CreateModel(
            name="OOIInformation",
            fields=[
                (
                    "id",
                    models.CharField(max_length=256, primary_key=True, serialize=False),
                ),
                ("last_updated", models.DateTimeField(auto_now=True)),
                ("data", models.JSONField(null=True)),
                ("consult_api", models.BooleanField(default=False)),
            ],
        ),
    ]
