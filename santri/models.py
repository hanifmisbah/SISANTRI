from django.db import models
from adminpondok.models import Pengumuman as pngm_models
# Create your models here.


class Pngm(models.Model):
    pngm = models.ForeignKey(pngm_models, on_delete=models.CASCADE)
