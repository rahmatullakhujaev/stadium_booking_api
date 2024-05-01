# Generated by Django 5.0.4 on 2024-05-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('status', models.SmallIntegerField(choices=[(1, 'active'), (2, 'canceled'), (3, 'booked')], default=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
