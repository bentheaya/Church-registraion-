from django.shortcuts import render, redirect
from .forms import MemberForm


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
