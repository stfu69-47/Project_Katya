"""
URL configuration for travel_guide project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from places.views import *
from places.views import page_not_found
from travel_guide import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('places.urls')),
    path('users/', include('users.urls', namespace = 'users')),
    path('api/v1/place/', PlaceAPIList.as_view()), #список мест
    path('api/v1/place/<int:pk>/', PlaceAPIUpdate.as_view()), #редактирование элемента
    path('api/v1/placedelete/<int:pk>/', PlaceAPIDestroy.as_view()), #удаление элемента
    path('api/v1/drf-auth/', include('rest_framework.urls')), #login
]

handler404 = page_not_found

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Панель администрирования'
admin.site.index_title = 'Места в Костромской области'