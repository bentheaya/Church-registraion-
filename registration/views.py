from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import MemberForm
from django.contrib.auth.forms import UserCreationForm
import json
from django.db.models import Count
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

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return HttpResponse('Unauthorized', status=401)
    members = User.objects.filter(is_staff=False)
    gender_distribution = Member.objects.values('gender').annotate(count=Count('gender'))
    age_distribution = Member.objects.values('date_of_birth').annotate(count=Count('date_of_birth'))

    gender_data = json.dumps(list(gender_distribution))
    age_data = json.dumps(list(age_distribution))

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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_admin = form.save()
            new_admin.is_staff = True
            new_admin.save()
            return redirect('admin_dashboard')
    else:
        form = UserCreationForm()
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
