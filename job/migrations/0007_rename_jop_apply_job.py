# Generated by Django 4.0.5 on 2022-07-05 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_apply_jop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='jop',
            new_name='job',
        ),
    ]
