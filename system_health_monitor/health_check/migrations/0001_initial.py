# Generated by Django 5.1.3 on 2024-11-06 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('OK', 'OK'), ('DOWN', 'DOWN')], max_length=50)),
                ('last_checked', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
