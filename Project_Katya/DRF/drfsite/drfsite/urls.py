"""
URL configuration for drfsite project.

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
from django.contrib import admin
from django.urls import path, include
from places.views import *
from rest_framework import routers


# router = routers.SimpleRouter()
# router.register(r'place', PlaceViewSet, basename='place')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/place/', PlaceAPIList.as_view()),
    path('api/v1/place/<int:pk>/', PlaceAPIUpdate.as_view()),
    path('api/v1/placedelete/<int:pk>/', PlaceAPIDestroy.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/', include(router.urls)), #http://127.0.0.1:8000/api/v1/place
    # path('api/v1/placelist/', PlaceViewSet.as_view({'get': 'list'})),
    # path('api/v1/placelist/<int:pk>/', PlaceViewSet.as_view({'put': 'update'})),
]
