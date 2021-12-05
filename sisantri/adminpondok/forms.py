from django.forms import ModelForm, widgets
from . import models

class SantriForm(ModelForm):
    class Meta:
        model=models.Santri
        exclude=[]

    # def __init__(self, *args, **kwargs):
    #     super(Santri, self).__init__(*args, **kwargs)
    #     self.fields['jk'].widget.attrs['class'] = 'form-control'
    
# class Pengajar(ModelForm):
#     class Meta:
#         model=models.Pengajar
#         field=['jk']