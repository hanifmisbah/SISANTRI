from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'adminpondok/dashboard.html')

def profil(req):
    return render(req, 'adminpondok/profil.html')