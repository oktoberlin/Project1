from django.shortcuts import render


def daftar_kelas(request):
    return render(request, 'daftar_kelas.html')