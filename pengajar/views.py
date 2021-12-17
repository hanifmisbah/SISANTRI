from typing import AsyncIterator
from django.shortcuts import redirect, render

from adminpondok import models
import pengajar

# Create your views here.


def index(req):
    return render(req, 'pengajar_dashboard.html')


def input_quran(req, id):
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

    quran = models.Pengajar.objects.all()
    return render(req, 'pengajar/input_quran.html', {
        'data': input_quran,
    })
