from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from testform.form import SignUpForm, LoginForm


def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('testform:login')

    return render(request, 'testform/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or wherever you want
                return redirect('testform:home')
            else:
                # Invalid login
                form.add_error(None, 'Invalid login credentials')
    else:
        form = LoginForm()

    return render(request, 'testform/login.html', {'form': form})


def home(request):
    return render(request, 'testform/home.html', {'form': SignUpForm()})

