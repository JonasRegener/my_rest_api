# Generated by Django 4.0.6 on 2022-11-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_alter_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.CharField(default='01-01-2000', max_length=10),
        ),
    ]
