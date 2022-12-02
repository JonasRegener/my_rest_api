# Generated by Django 4.0.6 on 2022-12-01 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_rename_task_subtask_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='subtasks',
            field=models.ManyToManyField(related_name='subtasks', to='todo.subtask'),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='todo',
            field=models.CharField(max_length=30),
        ),
    ]
