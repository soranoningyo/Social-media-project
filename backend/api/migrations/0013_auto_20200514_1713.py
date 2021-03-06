# Generated by Django 2.1.4 on 2020-05-14 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20200506_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conten', models.TextField()),
                ('publishedDate', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0)),
                ('ParentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Comments')),
                ('PostID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Essays')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'ذكر'), ('F', 'انثى')], default='غير محدد', max_length=6),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
