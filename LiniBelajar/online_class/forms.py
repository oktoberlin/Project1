from django import forms
from django.forms.widgets import ChoiceWidget, HiddenInput, RadioSelect
from .models import daftar_pre_toefl, daftar_english_todler, daftar_pre_ielts, Questionnaire

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



class AnswerForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        exclude = ['']
        widgets = {
            'field1': RadioSelect(choices=ChoiceWidget, attrs={'required': 'True'}),
            'field2': HiddenInput,
            }