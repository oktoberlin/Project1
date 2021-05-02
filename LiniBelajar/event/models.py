from django.db import models
from django.core.validators import RegexValidator

class daftar_talkshow(models.Model):
    nama_lengkap=models.CharField(verbose_name="Nama Lengkap",max_length=30)
    email=models.EmailField(max_length=200)
    phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    nomor_whatsapp = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    #message = models.CharField(max_length = 2000, default='Saya telah mendaftar kelas')