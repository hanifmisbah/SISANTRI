from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'adminpondok/dashboard.html')

def profil(req):
    return render(req, 'adminpondok/profil.html')

def datasantri(req):
    return render(req, 'adminpondok/datasantri.html')

def datapengajar(req):
    return render(req, 'adminpondok/datapengajar.html')

def datakitab(req):
    return render(req, 'adminpondok/datakitab.html')