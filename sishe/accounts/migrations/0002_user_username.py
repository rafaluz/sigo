# Generated by Django 3.0.5 on 2022-05-05 02:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=uuid.uuid4, max_length=150, unique=True),
        ),
    ]
