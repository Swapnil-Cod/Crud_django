# Generated by Django 4.0.4 on 2022-06-07 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_econtact_alter_employee_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='econtact',
            field=models.CharField(max_length=15),
        ),
    ]
