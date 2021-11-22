from django.shortcuts import redirect, render

from . import models, forms

# Create your views here.
def index(req):
    return render(req, 'adminpondok/dashboard.html')

def profil(req):
    return render(req, 'adminpondok/profil.html')

def datasantri(req):
#<<<<<<< HEAD
    #form = forms.Santri()
    if req.POST:
        #form = forms.Santri(req.POST)
        #if form.is_valid():
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
#=======
    # form = forms.Santri()
    if req.POST:
        # form = forms.Santri(req.POST)
        # if form.is_valid():
        #     form.save()
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
        return redirect('/adminpondok')
#>>>>>>> 5bb15c1d1b643226947612b8912a23478ce131cf

    santri = models.Santri.objects.all()
    return render(req, 'adminpondok/datasantri.html', {
        'data' : santri,
        #'form' : form,
    })

def datapengajar(req):
    #form = forms.Santri()
    if req.POST:
        #form = forms.Santri(req.POST)
        #if form.is_valid():
        #    form.save()
        models.Pengajar.objects.create(
             nama_pengajar=req.POST['nama_pengajar'],
             tempat_lahir=req.POST['tempat_lahir'],
             tanggal_lahir=req.POST['tanggal_lahir'],
             almt=req.POST['almt'],
             jk=req.POST['jk'],
             noind_pengajar=req.POST['noind_pengajar'],
             telp=req.POST['telp'],
             email=req.POST['email'],
             
         )
        return redirect('/adminpondok/datapengajar')

    pengajar = models.Pengajar.objects.all()
    return render(req, 'adminpondok/datapengajar.html', {
        'data' : pengajar,
        #'form' : form,
    })

def datakitab(req):
    return render(req, 'adminpondok/datakitab.html')

def quran(req):
    return render(req, 'adminpondok/quran.html')

def kitabkuning(req):
    return render(req, 'adminpondok/kitabkuning.html')

def deletepengajar(request, id):
    models.Pengajar.objects.filter(pk=id).delete()
    return redirect('/adminpondok/datapengajar')

def editpengajar(req, id):
    if request.POST:
        models.Pengajar.objects.filter(pk=id).update(
            nama_pengajar=req.POST['nama_pengajar'],
            tempat_lahir=req.POST['tempat_lahir'],
            tanggal_lahir=req.POST['tanggal_lahir'],
            almt=req.POST['almt'],
            jk=req.POST['jk'],
            noind_pengajar=req.POST['noind_pengajar'],
            telp=req.POST['telp'],
            email=req.POST['email'])
        return redirect('/')

    tasks = models.models.Pengajar.objects.all()
    return render(request, 'edit.html', {
    'data': tasks,
    })