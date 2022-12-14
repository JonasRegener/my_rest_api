# Generated by Django 4.0.6 on 2022-12-03 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0013_remove_subtask_todo_alter_todo_subtasks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='done',
            field=models.CharField(max_length=30),
        ),
        migrations.RemoveField(
            model_name='todo',
            name='subtasks',
        ),
        migrations.AddField(
            model_name='todo',
            name='subtasks',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='todo.subtask'),
        ),
    ]
