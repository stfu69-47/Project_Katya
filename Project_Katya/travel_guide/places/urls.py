from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('places/', Places.as_view(), name = 'places'),
    path('contact/', Contact.as_view(), name = 'contact'),
    path('feedback/', Feedback.as_view(), name = 'feedback'),
    path('about/', About.as_view(), name = 'about'),
    path('login/', login, name = 'login'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name = 'post'),
    path('addplace/', AddPostPlace.as_view(), name = 'addplace'),
    path('addperson/', AddPostPerson.as_view(), name = 'addperson'),
]