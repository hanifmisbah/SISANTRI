from django.forms import ModelForm
from . import models

class Santri(ModelForm):
    class Meta:
        model=models.Santri
        exclude=['nis', 'nama_santri', 'tempat_lahir', 'tanggal_lahir', 'almt', 'telp', 'email']
    
# class Pengajar(ModelForm):
#     class Meta:
#         model=models.Pengajar
#         field=['jk']