from django.shortcuts import render

# Create your views here.
from adminpondok import models
# from . import models


def index(req, id):
    pngm = models.Pengumuman.objects.all()
    pngmisi = models.Pengumuman.objects.filter(pk=id).first()

    return render(req, 'santri_dashboard.html', {
        'pngm': pngm,
        'pngmisi': pngmisi,
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
