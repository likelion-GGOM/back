# Generated by Django 4.2.3 on 2023-08-15 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='change_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
