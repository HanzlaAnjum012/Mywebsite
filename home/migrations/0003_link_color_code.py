# Generated by Django 3.2.12 on 2022-04-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220427_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='color_code',
            field=models.CharField(default='', max_length=40),
        ),
    ]
