from django.shortcuts import redirect, render

from . import models, forms

# Create your views here.


def index(req):
    return render(req, 'adminpondok/dashboard.html')


def profil(req):
    return render(req, 'adminpondok/profil.html')


def datasantri(req):
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
        return redirect('/adminpondok/datasantri')

    santri = models.Santri.objects.all()
    return render(req, 'adminpondok/datasantri.html', {
        'data': santri,
        # 'form' : form,
    })


def datapengajar(req):
    return render(req, 'adminpondok/datapengajar.html')


def datakitab(req):
    return render(req, 'adminpondok/datakitab.html')


def quran(req):
    return render(req, 'adminpondok/quran.html')


def kitabkuning(req):
    return render(req, 'adminpondok/kitabkuning.html')


def delete(req, id):
    models.Santri.objects.filter(pk=id).delete()  # pk = primary key
    return redirect('/adminpondok/datasantri')
