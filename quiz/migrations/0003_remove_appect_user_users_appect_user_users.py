# Generated by Django 4.2.7 on 2023-12-09 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("quiz", "0002_alter_task_options_appect_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="appect_user",
            name="users",
        ),
        migrations.AddField(
            model_name="appect_user",
            name="users",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
