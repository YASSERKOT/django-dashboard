# Generated by Django 2.1.7 on 2019-02-23 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_auto_20190223_2049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='userIDENTIFIER',
            new_name='userID',
        ),
    ]