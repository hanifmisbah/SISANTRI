from django.shortcuts import render
from adminpondok import models
from pengajar import models as models_pengajar


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
    # quran = models.Pengajar.objects.all()
    return render(req, 'ortu/hasil_quran.html')


def hasil_bandongan(req):
    return render(req, 'ortu/hasil_bandongan.html')


def hasil_matan(req):
    return render(req, 'ortu/hasil_matan.html')


def hasil_nadzom(req):
    return render(req, 'ortu/hasil_nadzom.html')


def hasil_sorogan(req):
    return render(req, 'ortu/hasil_sorogan.html')


def hasil(req):
    return render(req, 'ortu/hasil.html')
