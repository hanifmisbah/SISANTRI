from django.shortcuts import redirect, render

from . import models, forms
# from sisantri import adminpondok

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
    add_data = forms.SantriForm()

    if req.POST:
        add_data = forms.SantriForm(req.POST)

        if add_data.is_valid():
            add_data.save()
            return redirect('/adminpondok/datasantri')
    
    santri = models.Santri.objects.all()
    return render(req, 'adminpondok/datasantri.html', {
        'data': santri,
        'form': add_data,
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
        return redirect('/adminpondok/datasantri')

    tasks = models.Pengajar.objects.filter(pk=id).first()
    return render(req, 'adminpondok/editsantri.html', {
        'data1': tasks,
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
            pngjr=req.POST['pngjr'],

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


# ============D A T A  K I T A B=================

def datakitab(req):
    # form = forms.Santri()
    if req.POST:
        # form = forms.Santri(req.POST)
        # if form.is_valid():
        #    form.save()
        models.Kitab.objects.create(
            kode_kitab=req.POST['kode_kitab'],
            nama_kitab=req.POST['nama_kitab'],
            kategori_kitab=req.POST['kategori_kitab'],
            jenis_kitab=req.POST['jenis_kitab'],
            nama_pengarang=req.POST['nama_pengarang'],
        )
        return redirect('/adminpondok/datakitab')
    kitab = models.Kitab.objects.all()
    return render(req, 'adminpondok/datakitab.html', {
        'data': kitab,
        # 'form' : form,
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
        models.Pengumuman.objects.create(
            # tgl=req.POST['tgl'],
            judul=req.POST['judul'],
            pengumuman=req.POST['pengumuman'],
        )
        return redirect('/adminpondok')
    pengumuman = models.Pengumuman.objects.all()
    return render(req, 'adminpondok/pengumuman.html', {
        'data': pengumuman,
    })
