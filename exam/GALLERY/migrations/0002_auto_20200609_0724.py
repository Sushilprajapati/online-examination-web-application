# Generated by Django 3.0.5 on 2020-06-09 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GALLERY', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_image',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='add_image',
            name='s_img_id',
            field=models.IntegerField(default='0'),
        ),
    ]