# Generated by Django 3.0 on 2021-01-06 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20210104_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='category',
            field=models.CharField(max_length=50),
        ),
    ]
