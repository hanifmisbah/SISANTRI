from django.forms import ModelForm
from . import models

class Santri(ModelForm):
    model=models.Santri()
    exclude=[]