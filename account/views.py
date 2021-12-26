from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
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
            return redirect('/')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(req, 'register.html',{
        'form_regis':form,
        'msg':msg,
    })

def login_user(req):
    form = LoginForm(req.POST or None)
    msg = None
    if req.POST:
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(req, username=username, password=password)
            if user is not None and user.is_admin:
                login(req, user)
                return redirect('/adminpondok')
            elif user is not None and user.is_pengajar:
                login(req, user)
                return redirect('/pengajar')
            elif user is not None and user.is_pengasuh:
                login(req, user)
                return redirect('/pengasuh')
            elif user is not None and user.is_walisantri:
                login(req, user)
                return redirect('/ortu')
            elif user is not None and user.is_santri:
                login(req, user)
                return redirect('/santri')
            else:
                msg = 'invalid'
        else:
            msg = 'error validating form'
    return render(req, 'login.html',{
        'form':form,
        'msg':msg,
    })

def logout_user(req):
    logout(req)
    return redirect('/')