# Generated by Django 4.1.2 on 2022-11-09 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_uploadedfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(default=None, upload_to='uploadedFile'),
        ),
    ]