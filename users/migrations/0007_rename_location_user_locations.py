# Generated by Django 4.1.7 on 2023-03-13 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_managers_user_date_joined_user_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='location',
            new_name='locations',
        ),
    ]
