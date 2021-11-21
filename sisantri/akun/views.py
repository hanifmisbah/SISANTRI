from django.shortcuts import render

# Create your views here.
def login(req):
    return render(req, 'login.html')

def regis(req):
    return render(req, 'regis.html')