from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import MemberForm
from django.contrib.auth.forms import UserCreationForm
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseForbidden
from datetime import date
from django.contrib.auth import logout
from django.db.models import Count
from .forms import CustomUserCreationForm
from .models import CustomUser
from .models import Member
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()  # This ensures we are using the custom user model

def custom_admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_staff:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                # Return an 'invalid login' error message.
                return render(request, 'admin_login.html', {'form': form, 'error': 'Invalid credentials or not an admin.'})
    else:
        form = AuthenticationForm()
    return render(request, 'admin_login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('home')

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def group_ages(members):
    age_groups = {'0-10': 0, '11-20': 0, '21-30': 0, '31-40': 0, '41-50': 0, '51+': 0}
    for member in members:
        age = calculate_age(member['date_of_birth'])
        if 0 <= age <= 10:
            age_groups['0-10'] += 1
        elif 11 <= age <= 20:
            age_groups['11-20'] += 1
        elif 21 <= age <= 30:
            age_groups['21-30'] += 1
        elif 31 <= age <= 40:
            age_groups['31-40'] += 1
        elif 41 <= age <= 50:
            age_groups['41-50'] += 1
        else:
            age_groups['51+'] += 1
    return [{'age': k, 'count': v} for k, v in age_groups.items()]

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return HttpResponse('Unauthorized', status=401)
    
    members = Member.objects.all()
    gender_distribution = Member.objects.values('gender').annotate(count=Count('gender'))
    print(members)
    age_distribution = Member.objects.values('date_of_birth')
    age_data_list = group_ages(age_distribution)    

    gender_data = json.dumps(list(gender_distribution))
    age_data = json.dumps(age_data_list)

    return render(request, 'admin_dashboard.html', {
        'members': members,
        'gender_data': gender_data,
        'age_data': age_data
    })


@login_required
def create_admin(request):
    if not request.user.is_staff:
        return HttpResponse('Unauthorized', status=401)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_admin = form.save(commit=False)
            new_admin.is_staff = True
            new_admin.save()
            return redirect('admin_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'create_admin.html', {'form': form})

def home(request):
    return redirect('register')

def register(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = MemberForm()
    return render(request, 'registration/register.html', {'form': form})

def thank_you(request):
    return render(request, 'registration/thank_you.html')

@csrf_exempt  # manually handling CSRF 
def delete_member(request, member_id):
    if request.method == 'DELETE':
        
        member = get_object_or_404(Member, id=member_id)
        member.delete()
        return JsonResponse({'status': 'success'})
    else:
        return HttpResponseForbidden()

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Member

def member_details(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    data = {
        'full_name': member.full_name,
        'date_of_birth': member.date_of_birth,
        'gender': member.get_gender_display(),
        'phone_number': member.phone_number,
        'email_address': member.email_address,
        'mailing_address': member.mailing_address,
        'marital_status': member.get_marital_status_display(),
        'spouse_name': member.spouse_name,
        'children_names_ages': member.children_names_ages,
        'membership_status': member.get_membership_status_display(),
        'date_of_membership': member.date_of_membership,
        'baptism_info': member.baptism_info,
        'previous_church': member.previous_church,
        'ministry_interests': member.ministry_interests,
        'spiritual_gifts_talents': member.spiritual_gifts_talents,
        'emergency_contact_name': member.emergency_contact_name,
        'emergency_contact_relationship': member.emergency_contact_relationship,
        'emergency_contact_phone': member.emergency_contact_phone,
        'special_needs_allergies': member.special_needs_allergies,
        'preferred_service_time': member.preferred_service_time,
        'comments_notes': member.comments_notes,
        'photo_consent': member.photo_consent,
        'privacy_consent': member.privacy_consent,
    }
    return JsonResponse(data)
