# Generated by Django 5.1 on 2024-08-31 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Law_Assistant', '0003_rename_user_id_conversation_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='create_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='create_date',
            field=models.DateTimeField(),
        ),
    ]
