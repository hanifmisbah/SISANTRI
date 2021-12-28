from django.shortcuts import render
from adminpondok import models
from pengajar import models as models_pengajar
from santri.views import bandongan, matan, nadzom


def index(req):
    pngm = models.Pengumuman.objects.all()
    santri = models.Santri.objects.all()
    # pngm_d = models.Pengumuman.objects.filter(pk=id).first()
    return render(req, 'ortu/ortu_dashboard.html', {
        'pngm': pngm,
        'santri': santri
        # 'pngm_d': pngm_d,
    })


def detailpngm(req, id):
    pngm_d = models.Pengumuman.objects.filter(pk=id).first()
    return render(req, 'ortu/ortu_dashboard.html', {
        'pngm_d': pngm_d,
        # 'pngm': pngm,
    })


def hasil_quran(req):
    quran = models_pengajar.Alquran.objects.all()
    return render(req, 'ortu/hasil_quran.html', {
        'data': quran,
    })


def hasil_bandongan(req):
    bandongan = models_pengajar.Bandongan.objects.all()
    return render(req, 'ortu/hasil_bandongan.html', {
        'data': bandongan,
    })


def hasil_matan(req):
    matan = models_pengajar.Matan.objects.all()
    return render(req, 'ortu/hasil_matan.html', {
        'data': matan,
    })


def hasil_nadzom(req):
    nadzom = models_pengajar.Nadzom.objects.all()
    return render(req, 'ortu/hasil_nadzom.html', {
        'data': nadzom,
    })


def hasil_sorogan(req):
    sorogan = models_pengajar.Sorogan.objects.all()
    return render(req, 'ortu/hasil_sorogan.html', {
        'data': sorogan,
    })


def hasil(req):
    return render(req, 'ortu/hasil.html')
