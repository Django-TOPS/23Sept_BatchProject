# Generated by Django 3.0 on 2021-01-04 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='img',
            field=models.FileField(upload_to=''),
        ),
    ]
