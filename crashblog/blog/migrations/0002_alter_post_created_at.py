# Generated by Django 4.1.5 on 2023-02-23 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.TimeField(auto_now_add=True),
        ),
    ]