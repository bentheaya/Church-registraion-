from django.db import models

class Member(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
    ]
    MEMBERSHIP_STATUS_CHOICES = [
        ('N', 'New member'),
        ('E', 'Existing member'),
        ('V', 'Visitor'),
    ]

    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()
    mailing_address = models.CharField(max_length=255)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS_CHOICES)
    spouse_name = models.CharField(max_length=100, blank=True, null=True)
    children_names_ages = models.TextField(blank=True, null=True)
    membership_status = models.CharField(max_length=1, choices=MEMBERSHIP_STATUS_CHOICES)
    date_of_membership = models.DateField()
    baptism_info = models.CharField(max_length=255, blank=True, null=True)
    previous_church = models.CharField(max_length=255, blank=True, null=True)
    ministry_interests = models.CharField(max_length=255, blank=True, null=True)
    spiritual_gifts_talents = models.CharField(max_length=255, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_relationship = models.CharField(max_length=50)
    emergency_contact_phone = models.CharField(max_length=15)
    special_needs_allergies = models.TextField(blank=True, null=True)
    preferred_service_time = models.TimeField(blank=True, null=True)
    comments_notes = models.TextField(blank=True, null=True)
    photo_consent = models.BooleanField(default=False)
    privacy_consent = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
