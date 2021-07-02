from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from pwdmanager.decorators import login_required
from home.forms import LoginForm
from passkey.models import Passkey

@login_required
def indexView(request):
    if request.method=='GET':
        context = {'passkeys' : Passkey.objects.filter(user=request.user)}
        return render(request, 'index.html', context)

def loginView(request):
    context = {}

    if request.method == "GET":
        form = LoginForm()
        context['form'] = form
    else:
        form = LoginForm(data=request.POST)
        context['form'] = form
        if form.is_valid():
            user = authenticate(
                request, 
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('home:index')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'Invalid username or password'
            )    

    return render(request, 'login.html', context)

def logoutView(request):
    logout(request)
    return redirect('home:index')