from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LoginForm
# Create your views here.

def index(req):
    return render(req, 'login.html')

def regis(req):
    msg = None
    if req.POST:
        form = SignUpForm(req.POST)
        if form.is_valid():
            user = form.save()
            msg = 'User Created'
            return redirect('login.html')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(req, 'register.html',{
        'form_regis':form,
        'msg':msg,
    })

def login(req):
    form = LoginForm(req.POST or None)
    msg = None
    if req.POST:
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                return redirect('account')
            else:
                msg = 'invalid'
        else:
            msg = 'error validating form'
    return render(req, 'login.html',{
        'form':form,
        'msg':msg,
    })