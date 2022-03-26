# Generated by Django 3.0 on 2022-03-26 14:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='userid',
            field=models.CharField(default=uuid.UUID('e5de8a13-c861-4db6-86f3-4daeea974a14'), max_length=2255, unique=True),
        ),
    ]
