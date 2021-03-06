from typing import AsyncIterator
from django.db.models import query
from django.shortcuts import redirect, render
from adminpondok import models as admin_models
from adminpondok.views import alquran
from sisantri.settings import cursor, DB
from . import models

# Create your views here.

def index(req):
    santri = admin_models.Santri.objects.order_by('-id')
    pngm = admin_models.Pengumuman.objects.all()
    return render(req, 'pengajar/pengajar_dashboard.html', {
        'data': santri,
        'pngm': pngm,
    })


def pengumuman(req):
    pngm = admin_models.Pengumuman.objects.all()
    return render(req, 'pengajar/pengajar_dashboard.html', {
        'pngm': pngm,
    })

# def choose_santri(req):
#     if req

def input_inha(req):
    if req.POST:
        tgl=req.POST['tgl']
        surah=req.POST['surah']
        ayat=req.POST['ayat']
        juz=req.POST['juz']
        halaman=req.POST['halaman']
        pengajar=req.POST['pengajar']
        keterangan=req.POST['keterangan']

        query = "INSERT INTO Alquran (tgl, surah, ayat, juz, halaman, pengajar, keterangan) VALUES ('{0}', '{1}','{2}','{3}','{4}','{5}','{6}' )"
        variabel = (tgl, surah, ayat, juz, halaman, pengajar, keterangan)
        cursor.execute(query.format(variabel))
        DB.commit()
        data_quran = cursor.fetchall()

    return render(req, 'pengajar/pengajar_input_quran.html', {'quran': data_quran})


# =============== Q U R A N =====================


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


def deletequran(req, id):
    models.Alquran.objects.filter(pk=id).delete()
    return redirect('/pengajar/input_quran')

# ================== M A T A N ====================


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


def deletematan(req, id):
    models.Matan.objects.filter(pk=id).delete()
    return redirect('/pengajar/input_matan')

# =================== S O R O G A N ====================


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


def deletesorogan(req, id):
    models.Sorogan.objects.filter(pk=id).delete()
    return redirect('/pengajar/input_sorogan')

# ============== B A N D O N G A N ==============


def input_bandongan(req):
    if req.POST:
        models.Bandongan.objects.create(
            kitab=req.POST['kitab'],
            halaman=req.POST['halaman'],
            paragraf=req.POST['paragraf'],
            pengajar=req.POST['pengajar'],
        )
        return redirect('/pengajar/input_bandongan')

    bandongan = models.Bandongan.objects.all()
    return render(req, 'pengajar/pengajar_input_bandongan.html', {
        'data': bandongan,
    })


def deletebandongan(req, id):
    models.Bandongan.objects.filter(pk=id).delete()
    return redirect('/pengajar/input_bandongan')


def input_nadzom(req):
    if req.POST:
        models.Nadzom.objects.create(
            kitab=req.POST['kitab'],
            bab=req.POST['bab'],
            bait=req.POST['bait'],
            kelancaran=req.POST['kelancaran'],
            pengajar=req.POST['pengajar'],
            keterangan=req.POST['keterangan'],
        )
        return redirect('/pengajar/input_nadzom')

    ndzm = models.Nadzom.objects.all()
    return render(req, 'pengajar/pengajar_input_nadzom.html', {
        'data': ndzm,
    })


def deletenadzom(req, id):
    models.Nadzom.objects.filter(pk=id).delete()
    return redirect('/pengajar/input_nadzom')


def input(req):
    return render(req, 'pengajar/input.html')
