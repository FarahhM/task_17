# Generated by Django 2.0.4 on 2018-04-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(null=True, upload_to='restaurant_logos'),
        ),
    ]
