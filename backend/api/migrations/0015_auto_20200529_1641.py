# Generated by Django 2.1.4 on 2020-05-29 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20200514_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='ParentID',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='PostID',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
