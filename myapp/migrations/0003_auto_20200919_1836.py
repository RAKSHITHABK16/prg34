# Generated by Django 3.0.8 on 2020-09-19 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessdetails',
            name='datetime',
            field=models.DateTimeField(verbose_name='%Y-%m-%d %H:%M:%s'),
        ),
    ]
