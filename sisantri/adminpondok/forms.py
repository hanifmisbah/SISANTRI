from django.forms import ModelForm, widgets
from . import models

class Santri(ModelForm):

    class Meta:
        model=models.Santri
        fields=['jk', 'ktgri']
        widgets = {
            'jk' : widgets.RadioSelect(attrs={'class': 'Santri'}),
            'ktgri' : widgets.CheckboxSelectMultiple(attrs={'class': 'Santri'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(Santri, self).__init__(*args, **kwargs)
    #     self.fields['jk'].widget.attrs['class'] = 'form-control'
    
# class Pengajar(ModelForm):
#     class Meta:
#         model=models.Pengajar
#         field=['jk']