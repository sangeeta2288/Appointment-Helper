# Generated by Django 2.0.2 on 2018-02-23 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_text', models.CharField(max_length=200)),
                ('appointment_date_time', models.DateTimeField(verbose_name='appointment date time')),
            ],
        ),
    ]