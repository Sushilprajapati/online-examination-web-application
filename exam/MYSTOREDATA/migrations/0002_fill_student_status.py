# Generated by Django 3.0.5 on 2020-06-03 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MYSTOREDATA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fill_student',
            name='status',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
