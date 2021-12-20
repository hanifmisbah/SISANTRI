from django.shortcuts import redirect, render
from django.contrib import messages

from . import models, forms
# from sisantri import adminpondok


def coba(req):
    return render(req, 'coba.html')
# ============D A S H B O A R D=================


def index(req):
    santri = models.Santri.objects.all()
    pengajar = models.Pengajar.objects.all()
    quran = models.Alquran.objects.all()
    pengum = models.Pengumuman.objects.all()
    return render(req, 'adminpondok/dashboard.html', {
        'santri': santri,
        'pengajar': pengajar,
        'quran': quran,
        'pengum': pengum,
    })


def profil(req):
    return render(req, 'adminpondok/profil.html')


# ============S A N T R I=================

def datasantri(req):
    if req.POST:
        sntr = models.Santri.objects.create(
            nis=req.POST['nis'],
            nama_santri=req.POST['nama_santri'],
            tempat_lahir=req.POST['tempat_lahir'],
            tanggal_lahir=req.POST['tanggal_lahir'],
            jk=req.POST['jk'],
            almt=req.POST['almt'],
            telp=req.POST['telp'],
            email=req.POST['email'],
            ktgri=req.POST.getlist('ktgri'),
        )
        messages.info(req, f'Santri {sntr.nama_santri} Berhasil Di Tambah')
        return redirect('/adminpondok/datasantri')

    santri = models.Santri.objects.all()
    return render(req, 'adminpondok/datasantri.html', {
        'data': santri,
    })


def detailsantri(req, id):
    santri_det = models.Santri.objects.filter(pk=id).first()
    return render(req, 'adminpondok/datasantri.html', {
        'data': santri_det,
    })


def deletesantri(req, id):
    sntr = models.Santri.objects.filter(pk=id).delete()  # pk = primary key
    messages.info(req, f'Santri Berhasil Di Hapus')
    return redirect('/adminpondok/datasantri')


def editsantri(req, id):
    if req.POST:
        sntr = models.Santri.objects.filter(pk=id).update(
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
        messages.info(req, f'Santri {sntr.nama_santri} Berhasil Di Edit')
        return redirect('/adminpondok/datasantri')

    tasks = models.Santri.objects.filter(pk=id).first()
    return render(req, 'adminpondok/editsantri.html', {
        'data': tasks,
    })


# ============P E N G A J A R=================

def datapengajar(req):
    if req.POST:
        models.Pengajar.objects.create(
            NIP=req.POST['NIP'],
            nama_pengajar=req.POST['nama_pengajar'],
            tempat_lahir=req.POST['tempat_lahir'],
            tanggal_lahir=req.POST['tanggal_lahir'],
            almt=req.POST['almt'],
            jk=req.POST['jk'],
            telp=req.POST['telp'],
            email=req.POST['email'],
            pngjr=req.POST.getlist('pngjr'),

        )
        return redirect('/adminpondok/datapengajar')

    pengajar = models.Pengajar.objects.order_by('-id')
    return render(req, 'adminpondok/datapengajar.html', {
        'data': pengajar,
    })


def editpengajar(req, id):
    if req.POST:
        pngjr = models.Pengajar.objects.filter(pk=id).update(
            NIP=req.POST['NIP'],
            nama_pengajar=req.POST['nama_pengajar'],
            tempat_lahir=req.POST['tempat_lahir'],
            tanggal_lahir=req.POST['tanggal_lahir'],
            almt=req.POST['almt'],
            jk=req.POST['jk'],
            telp=req.POST['telp'],
            email=req.POST['email'],
            pngjr=req.POST['pngjr'],

        )
        messages.info(req, f'Pengajar {pngjr.nama_pengajar} Berhasil Di Edit')
        return redirect('/adminpondok/datapengajar')

    data = models.Pengajar.objects.filter(pk=id).first()
    return render(req, 'adminpondok/editpengajar.html', {
        'data': data,
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


# ============ N A D Z O M =================

def nadzom(req):
    if req.POST:
        models.Nadzom.objects.create(
            kode_kitab=req.POST['kode_kitab'],
            nama_kitab=req.POST['nama_kitab'],
            kategori_kitab=req.POST['kategori_kitab'],
            jumlah_bab=req.POST['jumlah_bab'],
            jumlah_fashol=req.POST['jumlah_fashol'],
            jumlah_bait=req.POST['jumlah_bait'],
            nama_pengarang=req.POST['nama_pengarang'],

        )
    elif req.POST:
        models
        return redirect('/adminpondok/nadzom')
    kitab = models.Nadzom.objects.all()
    return render(req, 'adminpondok/datakitab.html', {
        'data': kitab,
    })


# def editkitab(req, id):
#     if req.POST:
#      models.Kitab.objects.filter(pk=id).update(
#         kode_kitab=req.POST['kode_kitab'],
#             nama_kitab=req.POST['nama_kitab'],
#             kategori_kitab=req.POST['kategori_kitab'],
#             jenis_kitab=req.POST['jenis_kitab'],
#             nama_pengarang=req.POST['nama_pengarang'],
#     return redirect('/')

# tasks=models.Pengajar.objects.all()
# return render(req, 'editkitab.html', {
#     'data': task,
#     })


def deletekitab(req, id):
    models.Kitab.objects.filter(pk=id).delete()
    return redirect('/adminpondok/datakitab')

# ================ P E N G U M U M A N ===========


def pengumuman(req):
    if req.POST:
        pngm = models.Pengumuman.objects.create(
            # tgl=req.POST['tgl'],
            judul=req.POST['judul'],
            pengumuman=req.POST['pengumuman'],
        )
        messages.info(
            req, f'{pngm.judul} Pengumuman baru berhasil ditambahkan')
        return redirect('/adminpondok')
    pengumuman = models.Pengumuman.objects.all()
    return render(req, 'adminpondok/pengumuman.html', {
        'data': pengumuman,
    })


def deletepngm(req, id):
    pngm = models.Pengumuman.objects.filter(pk=id).delete()
    messages.info(req, f'Pengumuman berhasil dihapus')
    return redirect('/adminpondok')


def detailpngm(req, id):
    pngm = models.Pengumuman.objects.filter(pk=id).first()
    return render(req, 'adminpondok/dashboard.html', {
        'data': pngm,
    })
