from django.shortcuts import render

# Create your views here.
from adminpondok import models
from pengajar import models
# from . import models


def index(req):
    pngm = models.Pengumuman.objects.all()
    # pngmisi = models.Pengumuman.objects.filter(pk=id).first()

    return render(req, 'santri/santri_dashboard.html', {
        'pngm': pngm,
        # 'pngmisi': pngmisi,
    })


def quran(req):
    return render(req, 'santri/quran.html')


def bandongan(req):
    return render(req, 'santri/bandongan.html')


def matan(req):
    return render(req, 'santri/matan.html')


def nadzom(req):
    return render(req, 'santri/nadzom.html')


def sorogan(req):
    return render(req, 'santri/sorogan.html')
