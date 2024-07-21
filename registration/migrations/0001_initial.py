# Generated by Django 5.0.6 on 2024-07-21 21:42

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('phone_number', models.CharField(max_length=15)),
                ('email_address', models.EmailField(max_length=254)),
                ('mailing_address', models.CharField(max_length=255)),
                ('marital_status', models.CharField(choices=[('S', 'Single'), ('M', 'Married'), ('D', 'Divorced'), ('W', 'Widowed')], max_length=1)),
                ('spouse_name', models.CharField(blank=True, max_length=100, null=True)),
                ('children_names_ages', models.TextField(blank=True, null=True)),
                ('membership_status', models.CharField(choices=[('N', 'New member'), ('E', 'Existing member'), ('V', 'Visitor')], max_length=1)),
                ('date_of_membership', models.DateField()),
                ('baptism_info', models.CharField(blank=True, max_length=255, null=True)),
                ('previous_church', models.CharField(blank=True, max_length=255, null=True)),
                ('ministry_interests', models.CharField(blank=True, max_length=255, null=True)),
                ('spiritual_gifts_talents', models.CharField(blank=True, max_length=255, null=True)),
                ('emergency_contact_name', models.CharField(max_length=100)),
                ('emergency_contact_relationship', models.CharField(max_length=50)),
                ('emergency_contact_phone', models.CharField(max_length=15)),
                ('special_needs_allergies', models.TextField(blank=True, null=True)),
                ('preferred_service_time', models.TimeField(blank=True, null=True)),
                ('comments_notes', models.TextField(blank=True, null=True)),
                ('photo_consent', models.BooleanField(default=False)),
                ('privacy_consent', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
