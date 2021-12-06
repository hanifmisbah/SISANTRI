from django.shortcuts import render

# Create your views here.
from adminpondok import models
# from . import models


def index(req):
    pngm = models.Pengumuman.objects.all()
    return render(req, 'santri_dashboard.html', {
        'pngm': pngm
    })
