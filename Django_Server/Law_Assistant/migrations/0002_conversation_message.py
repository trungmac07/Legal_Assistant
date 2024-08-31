# Generated by Django 5.1 on 2024-08-31 05:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Law_Assistant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversation_name', models.CharField(max_length=100)),
                ('create_date', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateField()),
                ('sender', models.CharField(max_length=4)),
                ('text', models.TextField()),
                ('conversation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Law_Assistant.conversation')),
            ],
        ),
    ]
