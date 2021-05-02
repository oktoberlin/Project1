from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    terms = forms.BooleanField(
        error_messages={'required': 'Persyaratan dan Kondisi belum dicentang.'},
        label = "Disclaimer: Dengan memilih centang, anda menyetujui bahwa konten yang anda bagikan valid dan dipertanggungjawabkan penuh oleh akun anda. Linibelajar tidak bertanggungjawab atas ketidakvalidan info yang anda bagikan. Kami akan otomatis memblokir akun dengan konten SARA, provokasi dan pornografi."
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2', 'terms']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
