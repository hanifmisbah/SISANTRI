from django.shortcuts import render

# Create your views here.
from adminpondok import models
from pengajar import models as pengajar_models
# from . import models


def index(req):
    pngm = models.Pengumuman.objects.all()
    # pngmisi = models.Pengumuman.objects.filter(pk=id).first()

    return render(req, 'santri/santri_dashboard.html', {
        'pngm': pngm,
        # 'pngmisi': pngmisi,
    })


def quran(req):
    quran = pengajar_models.Alquran.objects.all()
    return render(req, 'santri/quran.html', {
        'data': quran,
    })


def bandongan(req):
    bandongan = pengajar_models.Bandongan.objects.all()
    return render(req, 'santri/bandongan.html', {
        'data': bandongan,
    })


def matan(req):
    matan = pengajar_models.Matan.objects.all()
    return render(req, 'santri/matan.html', {
        'data': matan,
    })


def nadzom(req):
    nadzom = pengajar_models.Nadzom.objects.all()
    return render(req, 'santri/nadzom.html', {
        'data': nadzom,
    })


def sorogan(req):
    sorogan = pengajar_models.Sorogan.objects.all()
    return render(req, 'santri/sorogan.html', {
        'data': sorogan,
    })
