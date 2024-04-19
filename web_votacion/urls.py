"""
URL configuration for web_votacion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from web_votacion_ocr import views
from django.conf import settings
from django.conf.urls.static import static
from .views import index


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('lista/', views.list_actas, name='list_actas'),
    path('subir_actas/', views.upload_actas, name='upload_actas'),
    path('datos_actas/', views.data_actas, name='data_actas'),
    path('admin/', admin.site.urls),
    path('index_text/', views.index_test, name='index_test'),
    path('subir/', views.procesar_imagen_view, name='subir_imagen'),
    path('imagen/<int:pk>/', views.ver_imagen_view, name='ver_imagen'),
    path('', index, name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
