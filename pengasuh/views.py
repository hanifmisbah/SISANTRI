from django.shortcuts import render
from adminpondok import models
from pengajar import models


# Create your views here.


def index(req):
    pngm = models.Pengumuman.objects.all()
    santri = models.Santri.objects.all()
    return render(req, 'pengasuh/pengasuh_dashboard.html', {
        'pngm': pngm,
        'santri': santri
    })


def hasil(req):
    return render(req, 'pengasuh/hasil.html')


def pengasuh_quran(req):
    return render(req, 'pengasuh/pengasuh_quran.html')


def pengasuh_matan(req):
    return render(req, 'pengasuh/pengasuh_matan.html')


def pengasuh_nadzom(req):
    return render(req, 'pengasuh/pengasuh_nadzom.html')


def pengasuh_sorogan(req):
    return render(req, 'pengasuh/pengasuh_sorogan.html')


def pengasuh_bandongan(req):
    return render(req, 'pengasuh/pengasuh_bandongan.html')


# butuh deff untuk memanggil nama santri satu persatu
