from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from .forms import daftar_talkshow_form
from django.core.mail import send_mail, BadHeaderError


def talkshow_add(request):
    # if this is a POST request we need to process the form data
    form = daftar_talkshow_form(request.POST)
    name = request.POST.get('name', '')
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = forms.daftar_pre_toefl_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('nama_lengkap')
            
            
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #if 'english_todler' in request.POST:
            subject = "Pendaftaran Talkshow 8 Mei 2021"
            body = {
            'nama_lengkap': form.cleaned_data['nama_lengkap'],
            'email': form.cleaned_data['email'],
            'phone_number': form.cleaned_data['phone_number'],
            #'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            
            
            messages.success(
                request, f'Halo {username}, Data anda sukses tersimpan! Link Zoom meeting bisa di cek di email. Tim kami juga akan mengirim linknya melalui Whatsapp')
            try:
                send_mail(subject, message, 'linibelajar@gmail.com',
                        ['marthasitanggang@ymail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            
            subject2 = "Pendaftaran Talkshow 8 Mei 2021 berhasil!"
            email = form.cleaned_data.get('email')
            body2 = {
            'nama_lengkap': form.cleaned_data['nama_lengkap']
            }
            
            message2 = "Terima kasih telah mendaftar. Pendaftaran Talkshow dengan tema Guru Penggerak dalam Gebrakan Merdeka Belajar telah berhasil. Berikut adalah link zoom meeting untuk hari Sabtu, 8 Mei 2021. Zoom Meeting: https://us02web.zoom.us/j/85349875762
"
            try:
                send_mail(subject2, message2, settings.EMAIL_HOST_USER, [email], fail_silently=False)
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
        form = daftar_talkshow_form()

    return render(request, 'event_form.html', {'form': form})

