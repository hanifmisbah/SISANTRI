from django.http import request
from django.shortcuts import redirect, render

from . import models, forms

# ============D A S H B O A R D=================


def index(req):
    santri = models.Santri.objects.all()
    pengajar = models.Pengajar.objects.all()
    quran = models.Alquran.objects.all()
    return render(req, 'adminpondok/dashboard.html', {
        'santri': santri,
        'pengajar': pengajar,
        'quran': quran,
    })


def profil(req):
    return render(req, 'adminpondok/profil.html')


# ============S A N T R I=================

def datasantri(req):
    # form = forms.Santri()
    if req.POST:
        # form = forms.Santri(req.POST)
        # if form.is_valid():
        #    form.save()
        models.Santri.objects.create(
            nis=req.POST['nis'],
            nama_santri=req.POST['nama_santri'],
            tempat_lahir=req.POST['tempat_lahir'],
            tanggal_lahir=req.POST['tanggal_lahir'],
            jk=req.POST['jk'],
            almt=req.POST['almt'],
            telp=req.POST['telp'],
            email=req.POST['email'],
            ktgri=req.POST['ktgri'],
        )
        return redirect('/adminpondok/datasantri')
    santri = models.Santri.objects.all()
    return render(req, 'adminpondok/datasantri.html', {
        'data': santri,
        # 'form' : form,
    })


def deletesantri(req, id):
    models.Santri.objects.filter(pk=id).delete()  # pk = primary key
    return redirect('/adminpondok/datasantri')


def editsantri(req, id):
    if req.POST:
        models.Santri.objects.filter(pk=id).update(
            nis=req.POST['nis'],
            nama_santri=req.POST['nama_santri'],
            tempat_lahir=req.POST['tempat_lahir'],
            tanggal_lahir=req.POST['tanggal_lahir'],
            jk=req.POST['jk'],
            almt=req.POST['almt'],
            telp=req.POST['telp'],
            email=req.POST['email'],
            ktgri=req.POST['ktgri'],
        )
        return redirect('/')

    tasks = models.Pengajar.objects.filter(pk=id).first()
    return render(req, 'edit.html', {
        'data': tasks,
    })


# ============P E N G A J A R=================

def datapengajar(req):
    # form = forms.Santri()
    if req.POST:
        # form = forms.Santri(req.POST)
        # if form.is_valid():
        #    form.save()
        models.Pengajar.objects.create(
            NIP=req.POST['NIP'],
            nama_pengajar=req.POST['nama_pengajar'],
            tempat_lahir=req.POST['tempat_lahir'],
            tanggal_lahir=req.POST['tanggal_lahir'],
            almt=req.POST['almt'],
            jk=req.POST['jk'],
            telp=req.POST['telp'],
            email=req.POST['email'],

        )
        return redirect('/adminpondok/datapengajar')

    pengajar = models.Pengajar.objects.all()
    return render(req, 'adminpondok/datapengajar.html', {
        'data': pengajar,
        # 'form' : form,
    })


def editpengajar(req, id):
    if req.POST:
        models.Pengajar.objects.filter(pk=id).update(
            NIP=req.POST['NIP'],
            nama_pengajar=req.POST['nama_pengajar'],
            tempat_lahir=req.POST['tempat_lahir'],
            tanggal_lahir=req.POST['tanggal_lahir'],
            almt=req.POST['almt'],
            jk=req.POST['jk'],
            telp=req.POST['telp'],
            email=req.POST['email'])
        return redirect('/')

    tasks = models.Pengajar.objects.all()
    return render(req, 'edit.html', {
        'data': tasks,
    })


def deletepengajar(req, id):
    models.Pengajar.objects.filter(pk=id).delete()
    return redirect('/adminpondok/datapengajar')


# ============K I T A B  A L - Q U R ' A N=================

def alquran(req):
    if req.POST:
        models.Alquran.objects.create(
            surah=req.POST['surah'],
            ayat=req.POST['ayat'],
        )
        return redirect('/adminpondok/quran')

    quran = models.Alquran.objects.all()
    # det_surah = models.Alquran.objects.filter(pk=id).first()
    return render(req, 'adminpondok/quran.html', {
        'data': quran,
        # 'datasurah' : det_surah,
    })


def deletequran(req, id):
    models.Alquran.objects.filter(pk=id).delete()
    return redirect('/adminpondok/quran')


def detailquran(req, id):
    detail = models.Alquran.objects.filter(pk=id).first()
    return render(req, 'adminpondok/quran.html', {
        'data': detail,
    })


# ============K I T A B  K U N I N G=================

def kitabkuning(req):
    return render(req, 'adminpondok/kitabkuning.html')
