from django.db import models
from django.shortcuts import redirect, render
from adminpondok import models as pond_models

# Create your views here.


def index(req):
    data_santri = pond_models.Santri.objects.all()
    print(data_santri)
    konteks = { 'data' : data_santri } 
    return render(req, 'pengajar_dashboard.html' , konteks)

# def pengajar(req) :
#     return render(req, 'pengajar_dashboard.html')
