# Generated by Django 4.1 on 2022-09-20 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_Manage_sys_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]