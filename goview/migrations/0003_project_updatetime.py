# Generated by Django 4.1 on 2024-03-11 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='updateTime',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]
