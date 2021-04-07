from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import daftar_pre_toefl_form, daftar_english_todler_form, daftar_pre_ielts_form
from django.core.mail import send_mail, BadHeaderError


def daftar_kelas(request):
    return render(request, 'daftar_kelas.html')


def thanks(request):
    return render(request, 'thanks.html')


def pre_toefl_add(request):
    # if this is a POST request we need to process the form data
    form = daftar_pre_toefl_form(request.POST)
    name = request.POST.get('name', '')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = forms.daftar_pre_toefl_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #if 'english_todler' in request.POST:
            subject = "Pendaftaran Kelas Pre-TOEFL"
            body = {
            'nama_lengkap': form.cleaned_data['nama_lengkap'],
            'email': form.cleaned_data['email'],
            'phone_number': form.cleaned_data['phone_number'],
            #'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            
            try:
                send_mail(subject, message, 'oktoberlin@gmail.com',
                        ['marthasitanggang@ymail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("thanks")
            # register=form.save(commit=False)
            # register.nama_lengkap = request.POST.get('nama_lengkap')
            # register.email = request.POST.get('email')
            # register.phone_number = request.POST.get('phone_number')
            
            # return HttpResponseRedirect(reverse('/thanks/'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = daftar_pre_toefl_form()

    return render(request, 'pre_toefl.html', {'form': form})

def english_todler_add(request):
    # if this is a POST request we need to process the form data
    form = daftar_english_todler_form(request.POST)
    name = request.POST.get('name', '')
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        #form = forms.daftar_pre_toefl_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            subject = "Pendaftaran Kelas English for Todler"
            body = {
            'nama_lengkap': form.cleaned_data['nama_lengkap'],
            'email': form.cleaned_data['email'],
            'phone_number': form.cleaned_data['phone_number'],
            #'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            
            try:
                send_mail(subject, message, 'oktoberlin@gmail.com',
                        ['marthasitanggang@ymail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("thanks")
            # register=form.save(commit=False)
            # register.nama_lengkap = request.POST.get('nama_lengkap')
            # register.email = request.POST.get('email')
            # register.phone_number = request.POST.get('phone_number')
            
            # return HttpResponseRedirect(reverse('/thanks/'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = daftar_english_todler_form()

    return render(request, 'english_todler.html', {'form': form})


def pre_ielts_add(request):
    # if this is a POST request we need to process the form data
    form = daftar_pre_ielts_form(request.POST)
    name = request.POST.get('name', '')
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        #form = forms.daftar_pre_toefl_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            #form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            subject = "Pendaftaran Kelas Pre-IELTS"
            body = {
            'nama_lengkap': form.cleaned_data['nama_lengkap'],
            'email': form.cleaned_data['email'],
            'phone_number': form.cleaned_data['phone_number'],
            #'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            
            try:
                send_mail(subject, message, 'oktoberlin@gmail.com',
                        ['marthasitanggang@ymail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("thanks")
            # register=form.save(commit=False)
            # register.nama_lengkap = request.POST.get('nama_lengkap')
            # register.email = request.POST.get('email')
            # register.phone_number = request.POST.get('phone_number')
            
            # return HttpResponseRedirect(reverse('/thanks/'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = daftar_pre_ielts_form()

    return render(request, 'pre_ielts.html', {'form': form})