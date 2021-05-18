from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
UserModel = get_user_model()
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse

from django.shortcuts import render, redirect

from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import RegisterUserForm, UserUpdateForm, ProfileUpdateForm



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('community:community')
    else:
        form = RegisterUserForm()
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                username = form.cleaned_data.get('username')
                messages.success(
                    request, f'Hi {username}, Email Aktivasi Akun anda telah terkirim.')
                

                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('activate_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()

                return redirect('user:login')
        else:
            form = RegisterUserForm()
        return render(request, 'register.html', {'form': form})

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('community:community')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('community:community')
			else:
				messages.info(request, 'Username atau Password Salah')

		context = {}
		return render(request, 'login.html', context)

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(
                request, f'Terima kasih telah mengkonfirmasi emailnya. Sekarang anda bisa login.')
        return redirect('user:login')
    else:
        return HttpResponse('Link Aktivasi salah!')

def logoutUser(request):
	logout(request)
	return redirect('community:community')
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Akun Anda sukses diupdate')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)
