from django.shortcuts import render
from adminpondok import models as adminmodels
from pengajar import models as models_pengajar
from santri.views import matan, nadzom


# Create your views here.


def index(req):
    pngm = adminmodels.Pengumuman.objects.all()
    santri = adminmodels.Santri.objects.all()
    return render(req, 'pengasuh/pengasuh_dashboard.html', {
        'pngm': pngm,
        'santri': santri
    })


def hasil(req):
    return render(req, 'pengasuh/hasil.html')


def pengasuh_quran(req):
    quran = models_pengajar.Alquran.objects.all()
    return render(req, 'pengasuh/pengasuh_quran.html', {
        'data': quran,
    })


def pengasuh_bandongan(req):
    bandongan = models_pengajar.Bandongan.objects.all()
    return render(req, 'pengasuh/pengasuh_bandongan.html', {
        'data': bandongan,
    })


def pengasuh_matan(req):
    matan = models_pengajar.Matan.objects.all()
    return render(req, 'pengasuh/pengasuh_matan.html', {
        'data': matan,
    })


def pengasuh_nadzom(req):
    nadzom = models_pengajar.Nadzom.objects.all()
    return render(req, 'pengasuh/pengasuh_nadzom.html', {
        'data': nadzom,
    })


def pengasuh_sorogan(req):
    sorogan = models_pengajar.Sorogan.objects.all()
    return render(req, 'pengasuh/pengasuh_sorogan.html', {
        'data': sorogan,
    })


# butuh deff untuk memanggil nama santri satu persatu
