# Generated by Django 3.0.5 on 2020-06-03 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('STUDENT_DATA', '0005_auto_20200603_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_signup_record',
            old_name='college_name',
            new_name='username',
        ),
    ]