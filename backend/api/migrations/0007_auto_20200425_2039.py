# Generated by Django 2.1.4 on 2020-04-25 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200425_2007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='countris',
            new_name='countries',
        ),
    ]
