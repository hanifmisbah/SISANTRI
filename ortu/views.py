from django.shortcuts import render

# Create your views here.
from adminpondok import models


def index(req):
    pngm = models.Pengumuman.objects.all()
    return render(req, 'ortu_dashboard.html', {
        'pngm': pngm
    })


def quran(req):
    return render(req, 'quran.html')


def bandongan(req):
    return render(req, 'bandongan.html')


def matan(req):
    return render(req, 'matan.html')


def nadzom(req):
    return render(req, 'nadzom.html')


def sorogan(req):
    return render(req, 'sorogan.html')
