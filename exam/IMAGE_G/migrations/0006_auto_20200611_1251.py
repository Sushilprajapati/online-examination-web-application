# Generated by Django 3.0.5 on 2020-06-11 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMAGE_G', '0005_auto_20200611_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img_store',
            name='pic',
            field=models.ImageField(blank=True, default='/static/login.jpeg', upload_to='photos'),
        ),
    ]
