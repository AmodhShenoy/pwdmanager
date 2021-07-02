from django.shortcuts import render, redirect
from home.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from pwdmanager.decorators import login_required

@login_required
def indexView(request):
    return render(request, 'homePage.html')

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