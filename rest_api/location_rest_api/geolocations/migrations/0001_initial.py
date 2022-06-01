# Generated by Django 3.2.13 on 2022-06-01 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('telegram_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('telegram_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegram_users.telegramuser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
