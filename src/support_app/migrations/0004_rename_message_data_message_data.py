# Generated by Django 4.0.4 on 2022-04-18 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support_app', '0003_remove_ticketstatus_url_remove_userticket_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message_data',
            new_name='data',
        ),
    ]