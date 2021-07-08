from django import forms
from .models import daftar_pre_toefl, daftar_english_todler, daftar_pre_ielts

class daftar_pre_toefl_form(forms.ModelForm):
    nama_lengkap=forms.CharField()
    email=forms.EmailField()
    phone_number = forms.CharField()
    #message = forms.CharField(widget = forms.Textarea)
    class Meta:
        model= daftar_pre_toefl
        fields=['nama_lengkap','email','phone_number',]

class daftar_english_todler_form(forms.ModelForm):
    nama_lengkap=forms.CharField()
    email=forms.EmailField()
    phone_number = forms.CharField()
    #message = forms.CharField(widget = forms.Textarea)
    class Meta:
        model= daftar_english_todler
        fields=['nama_lengkap','email','phone_number',]

class daftar_pre_ielts_form(forms.ModelForm):
    nama_lengkap=forms.CharField()
    email=forms.EmailField()
    phone_number = forms.CharField()
    #message = forms.CharField(widget = forms.Textarea)
    class Meta:
        model= daftar_pre_ielts
        fields=['nama_lengkap','email','phone_number',]