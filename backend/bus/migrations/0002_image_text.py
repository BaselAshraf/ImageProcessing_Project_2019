# Generated by Django 2.2 on 2019-04-27 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
