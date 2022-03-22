# Generated by Django 2.2.26 on 2022-03-22 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentConnectApp', '0010_auto_20220322_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='blocks',
            field=models.ManyToManyField(blank=True, null=True, related_name='_student_blocks_+', to='StudentConnectApp.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='matches',
            field=models.ManyToManyField(blank=True, null=True, related_name='_student_matches_+', to='StudentConnectApp.Student'),
        ),
    ]
