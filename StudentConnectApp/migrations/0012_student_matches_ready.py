# Generated by Django 2.2.26 on 2022-03-23 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentConnectApp', '0011_auto_20220322_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='matches_ready',
            field=models.BooleanField(default=False),
        ),
    ]