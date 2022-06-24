# Generated by Django 4.0.5 on 2022-06-24 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_jop_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='jop',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='jop',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jop',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
    ]