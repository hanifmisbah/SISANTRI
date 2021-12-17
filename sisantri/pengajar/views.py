from django.db import models
from django.shortcuts import redirect, render
from adminpondok import models as pond_models

# Create your views here.


def index(req):
    data_santri = pond_models.Santri.objects.order_by('-id')
    data_pngm = pond_models.Pengumuman.objects.all()
    print(data_santri)
    print(data_pngm)
    # konteks = { 'data' : data_santri } 
    # pngm = { 'datapngm' : data_pngm } 
    return render(req, 'pengajar/pengajar_dashboard.html' , {
        'data' : data_santri,
        'datapngm' : data_pngm,
    })

def pengajar(req) :
    return render(req, 'pengajar/pengajar_dashboard.html')
