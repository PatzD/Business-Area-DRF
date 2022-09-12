# Generated by Django 4.1.1 on 2022-09-12 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="email",
        ),
        migrations.AddField(
            model_name="department",
            name="employees",
            field=models.ManyToManyField(
                blank=True, related_name="employees", to="api.employee"
            ),
        ),
        migrations.AddField(
            model_name="employee",
            name="last_raise",
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="employee",
            name="salary",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="employee",
            name="surname",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="employee",
            name="vacation_days",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="department",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="address",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="employee",
            name="id_mum",
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name="employee",
            name="name",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="employee",
            name="passport",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="employee",
            name="patronymic",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="employee",
            name="position",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="position",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]