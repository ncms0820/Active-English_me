# Generated by Django 3.2.5 on 2021-07-12 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0003_auto_20210708_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='activelecture',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='activelecture',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('canceled', 'Canceled')], default='pending', max_length=12),
        ),
    ]