# Generated by Django 4.2.4 on 2023-08-18 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_question_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
    ]
