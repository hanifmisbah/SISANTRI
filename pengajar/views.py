from typing import AsyncIterator
from django.shortcuts import redirect, render

from adminpondok import models as admin_models
from . import models
import pengajar
from pengajar.models import Sorogan

# Create your views here.


def index(req):
    santri = admin_models.Santri.objects.order_by('-id')
    return render(req, 'pengajar/pengajar_dashboard.html', {
        'data': santri,
    })


def pengumuman(req):
    pngm = admin_models.Pengumuman.objects.all()
    return render(req, 'pengajar/pengumuman.html', {
        'data': pngm,
    })


def input_quran(req):
    if req.POST:
        models.Alquran.objects.create(
            surah=req.POST['surah'],
            juz=req.POST['juz'],
            halaman=req.POST['halaman'],
            ayat=req.POST['ayat'],
            pengajar=req.POST['pengajar'],
            keterangan=req.POST['keterangan'],
        )
        return redirect('/pengajar/input_quran')

    quran = models.Alquran.objects.all()
    return render(req, 'pengajar/pengajar_input_quran.html', {
        'data': quran,
    })


def input_matan(req):
    if req.POST:
        models.Matan.objects.create(
            kitab=req.POST['kitab'],
            bab=req.POST['bab'],
            halaman=req.POST['halaman'],
            pengajar=req.POST['pengajar'],
            keterangan=req.POST['keterangan'],
        )
        return redirect('/pengajar/input_matan')

    matan = models.Matan.objects.all()
    return render(req, 'pengajar/pengajar_input_matan.html', {
        'data': matan,
    })


def input_sorogan(req):
    if req.POST:
        models.Sorogan.objects.create(
            kitab=req.POST['kitab'],
            bab=req.POST['bab'],
            halaman=req.POST['halaman'],
            paragraf=req.POST['paragraf'],
            pengajar=req.POST['pengajar'],
        )
        return redirect('/pengajar/input_sorogan')

    sorogan = models.Sorogan.objects.all()
    return render(req, 'pengajar/pengajar_input_sorogan.html', {
        'data': sorogan,
    })


def input_bandongan(req):
    if req.POST:
        models.Bandongan.objects.create(
            kitab=req.POST['kitab'],
            bab=req.POST['bab'],
            halaman=req.POST['halaman'],
            paragraf=req.POST['paragraf'],
            pengajar=req.POST['pengajar'],
        )
        return redirect('/pengajar/input_bandongan')

    bandongan = models.Bandongan.objects.all()
    return render(req, 'pengajar/pengajar_input_bandongan.html', {
        'data': bandongan,
    })


def input_nadzom(req):
    if req.POST:
        models.Nadzom.objects.create(
            kitab=req.POST['kitab'],
            bab=req.POST['bab'],
            bait=req.POST['bait'],
            pengajar=req.POST['pengajar'],
            keterangan=req.POST['keterangan'],
        )
        return redirect('/pengajar/input_nadzom')

    ndzm = models.Nadzom.objects.all()
    return render(req, 'pengajar/pengajar_input_nadzom.html', {
        'data': ndzm,
    })


def input(req):
    return render(req, 'pengajar/input.html')
