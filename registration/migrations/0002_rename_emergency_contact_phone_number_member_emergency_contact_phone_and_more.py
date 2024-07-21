# Generated by Django 5.0.6 on 2024-07-21 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='emergency_contact_phone_number',
            new_name='emergency_contact_phone',
        ),
        migrations.RemoveField(
            model_name='member',
            name='baptism_date',
        ),
        migrations.RemoveField(
            model_name='member',
            name='baptism_place',
        ),
        migrations.AddField(
            model_name='member',
            name='baptism_info',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='mailing_address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='member',
            name='ministry_interests',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='preferred_service_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='previous_church',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='spiritual_gifts_talents',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
