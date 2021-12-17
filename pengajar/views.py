from typing import AsyncIterator
from django.shortcuts import redirect, render

from adminpondok import models
import pengajar

# Create your views here.
def index(req):
    santri = models.Santri.objects.order_by('-id')
    return render(req, 'pengajar/pengajar_dashboard.html', {
        'data': santri,
    })



def pengumuman(req):
    pngm = models.Pengumuman.objects.all()
    return render(req, 'pengajar/pengumuman.html', {
        'data': pngm,
    })


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
