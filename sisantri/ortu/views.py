from django.shortcuts import render

# Create your views here.
from adminpondok import models


def index(req):
    pngm = models.Pengumuman.objects.all()
    return render(req, 'ortu_dashboard.html', {
        'pngm': pngm
    })
