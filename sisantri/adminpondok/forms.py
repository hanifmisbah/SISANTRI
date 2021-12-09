from django.db.models import fields
from django.forms import ModelForm, widgets
from . import models

class SantriForm(ModelForm):
    class Meta:
        model=models.Santri
        fields=['nis', 'nama_santri', 'tempat_lahir', 'tanggal_lahir', 'telp', 'email', 'jk', 'ktgri', 'almt']
        widgets={
            'nis' : widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nomor Induk Santri'}),
            'nama_santri' : widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Santri'}),
            'tempat_lahir' : widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tempat Lahir'}),
            'tanggal_lahir' : widgets.DateInput(format='%d/%m/%Y', attrs={'type': 'date', 'placeholder': 'Pilih Tanggal lahir'}),
            'telp' : widgets.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nomor Telepon'}),
            'email' : widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'jk' : widgets.RadioSelect(attrs={'class': 'form-control', 'placeholder': 'Jenis Kelamin'}),
            # 'ktgri' : widgets.CheckboxSelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Kategori'}),
            'almt' : widgets.Textarea(attrs={'class': 'form-control', 'placeholder': 'Alamat'}),
        }

    def __init__(self, *args, **kwargs):
        super(SantriForm, self).__init__(*args, **kwargs)
        self.fields['nis'].label=''
        self.fields['jk'].label=''
        self.fields['nama_santri'].label=''
        self.fields['tempat_lahir'].label=''
        self.fields['tanggal_lahir'].label=''
        self.fields['telp'].label=''
        self.fields['email'].label=''
        self.fields['ktgri'].widget.attrs['class'] = 'form-control'
        self.fields['ktgri'].label=''
        self.fields['almt'].label=''
    
# class Pengajar(ModelForm):
#     class Meta:
#         model=models.Pengajar
#         field=['jk']