from django.shortcuts import render
from adminpondok import models
# Create your views here.


def index(req):
    pngm = models.Pengumuman.objects.all()
    return render(req, 'pengasuh_dashboard.html', {
        'pngm': pngm
    })


def hasil(req):
    return render(req, 'hasil.html')


# butuh deff untuk memanggil nama santri satu persatu
