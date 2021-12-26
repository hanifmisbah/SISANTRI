from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('is admin', default=False)
    is_pengajar = models.BooleanField('is pengajar', default=False)
    is_pengasuh = models.BooleanField('is pengasuh', default=False)
    is_walisantri = models.BooleanField('is walisantri', default=False)
    is_santri = models.BooleanField('is santri', default=False)