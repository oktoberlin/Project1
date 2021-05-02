from django import forms
from .models import daftar_talkshow

class daftar_talkshow_form(forms.ModelForm):
    nama_lengkap=forms.CharField()
    email=forms.EmailField()
    nomor_whatsapp = forms.CharField()
    #message = forms.CharField(widget = forms.Textarea)
    class Meta:
        model= daftar_pre_toefl
        fields=['nama_lengkap','email','nomor_whatsapp',]