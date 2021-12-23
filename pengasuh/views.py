from django.shortcuts import render
from adminpondok import models
# Create your views here.


def index(req):
    pngm = models.Pengumuman.objects.all()
    return render(req, 'pengasuh_dashboard.html', {
        'pngm': pngm
    })

<<<<<<< HEAD

def sidebar(req):
    return render(req, 'sidebar.html')
=======
def sidebar(req):
    return render(req, 'sidebar.html')
>>>>>>> 9405731929915f06b6d81c9e9c102d995e42ef79
