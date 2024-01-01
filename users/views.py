from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def user_login(request):
    form = AuthenticationForm(request, request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'Successfully logged in.')
            return redirect('candidate_list')

    messages.error(request, 'Invalid login credentials.')
    return render(request, 'registration/user_login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('user_login')
