# Generated by Django 3.2.12 on 2022-04-27 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_link',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
