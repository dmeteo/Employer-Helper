# Generated by Django 5.1.3 on 2025-01-13 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_rename_recipient_notification_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name': 'Уведомление', 'verbose_name_plural': 'Уведомления'},
        ),
        migrations.AlterModelTable(
            name='notification',
            table='notifications',
        ),
    ]
