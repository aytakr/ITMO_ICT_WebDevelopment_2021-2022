# Generated by Django 4.0 on 2022-01-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks_app', '0003_studenthomework_done_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]