# Generated by Django 4.1.2 on 2022-11-13 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_secretkey'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SecretKey',
        ),
    ]
