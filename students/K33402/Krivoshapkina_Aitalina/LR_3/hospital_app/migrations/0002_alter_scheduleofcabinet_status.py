# Generated by Django 4.0 on 2022-01-15 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleofcabinet',
            name='status',
            field=models.BinaryField(default=0, verbose_name='Статус'),
        ),
    ]
