# Generated by Django 4.2.4 on 2023-08-17 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_remove_question_author_alter_question_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
