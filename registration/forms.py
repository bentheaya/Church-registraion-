from django import forms
from .models import Member
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'full_name', 'date_of_birth', 'gender', 'phone_number', 'email_address', 
            'mailing_address', 'marital_status', 'spouse_name', 'children_names_ages',
            'membership_status', 'date_of_membership', 'baptism_info', 'previous_church', 
            'ministry_interests', 'spiritual_gifts_talents', 'emergency_contact_name', 
            'emergency_contact_relationship', 'emergency_contact_phone', 'special_needs_allergies',
            'preferred_service_time', 'comments_notes', 'photo_consent', 'privacy_consent'
        ]

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'date_of_membership': forms.DateInput(attrs={'type': 'date'}),
            'preferred_service_time': forms.TimeInput(attrs={'type': 'time'}),
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
