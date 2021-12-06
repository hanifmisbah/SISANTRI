from django.shortcuts import redirect, render

# Create your views here.


def index(req):
    return render(req, 'pengajar_dashboard.html')
