from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views



from musicschool.contact.views import v1_urls

urlpatterns = [
    path('', include('etriolet.front.urls'),

    path('admin/', admin.site.urls, name='admin'),
    path('/register/', RegistrationView.as_view(), name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('backoffice/', include('etriolet.backoffice.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)