# Generated by Django 4.0.6 on 2025-04-08 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_alter_count_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='certificateSent',
            field=models.BooleanField(default=False),
        ),
    ]
