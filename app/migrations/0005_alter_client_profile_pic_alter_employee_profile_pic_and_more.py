# Generated by Django 4.0.5 on 2022-06-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_client_profile_pic_alter_employee_profile_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='cppic/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='eppic/'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='mppic/'),
        ),
    ]
