# Generated by Django 5.0.4 on 2024-05-30 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('times', '0010_alter_task_task_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calc',
            old_name='today',
            new_name='numsTask',
        ),
    ]
