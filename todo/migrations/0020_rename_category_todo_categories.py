# Generated by Django 4.0.6 on 2022-12-05 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0019_category_subtask_done_remove_todo_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='category',
            new_name='categories',
        ),
    ]
