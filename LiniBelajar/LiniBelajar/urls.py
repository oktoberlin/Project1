from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from user import views as user_views
from django.views.generic import TemplateView
from .views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point"),
]
# + static(settings.STATIC_URL,
#                          document_root=settings.STATIC_ROOT)


#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL,
#                          document_root=settings.MEDIA_ROOT)


