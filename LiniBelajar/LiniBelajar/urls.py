from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user import views as user_views
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('home.urls'), name='home'),
    path('store/', include('store.urls', namespace='store')),
    path('ecommerce/', include('ecommerce_app.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('about/', TemplateView.as_view(template_name='about.html')),
    path('komunitas', include('community.urls'), name='community'),
    path('kelas-online/', include('online_class.urls'), name='online_class'),
    path('talkshow/', include('event.urls'), name='event'),
    path('', include('user.urls')),
    path('', include('testvue.urls')),
    path('api/posts/', include('postAPI.urls')),
    path('api/user/', include('userAPI.urls')),
    path('api/user/profile/', include('profileAPI.urls')),
    #path('komunitas/', include('community.urls'), name='community'),
    #path('komunitas/', include('community.urls')),
    path('react/', TemplateView.as_view(template_name='react.html')),
    path('quizs', include('quiz.urls'), name='quiz'),
    path('admin/', admin.site.urls),
    #path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('accounts/', include('allauth.urls')),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-done', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name='password_reset_complete'),
] + static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


