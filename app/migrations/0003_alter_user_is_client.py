# Generated by Django 4.0.5 on 2022-06-23 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_user_is_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_client',
            field=models.BooleanField(default=False, verbose_name='client status'),
        ),
    ]
