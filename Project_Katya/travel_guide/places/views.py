from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .forms import *
from .filters import *
from .models import *
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .utils import *
from rest_framework import generics, viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import *
from .serializers import *


posts = Place.objects.all()


class PlaceAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


class PlaceAPIList(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PlaceAPIListPagination


class PlaceAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = IsOwnerOrReadOnly,


class PlaceAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = IsAdminReadOnly,


class Home(DataMixin, ListView):
    model = Place
    template_name = 'places/main.html'
    title_page = 'Главная страница'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        place_filter = PlaceFilter(self.request.GET, queryset)
        place_url = queryset.values_list()[0][2]
        return self.get_mixin_context(context, title = self.title_page, place_filter = place_filter, place_url = place_url)

    def get_queryset(self):
        queryset = super().get_queryset()
        place_filter = PlaceFilter(self.request.GET, queryset)
        return place_filter.queryset


class Places(DataMixin, ListView):
    model = Place
    template_name = 'places/places.html'
    title_page = 'Выбор места'
    context_object_name = 'posts'


class Feedback(DataMixin, ListView):
    model = Place
    template_name = 'places/feedback.html'
    title_page = 'Отзывы'


class Contact(DataMixin, ListView):
    model = Place
    template_name = 'places/contact.html'
    title_page = 'Контакты'


class About(DataMixin, ListView):
    model = Place
    template_name = 'places/about.html'
    title_page = 'О сайте'
    paginate_by = 3


def about(request):
    contact_list = Place.objects.filter(is_published=True)
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # if request.method == 'POST':
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         fp = Uploadfiles(file=form.cleaned_data.get('file'))
    #         fp.save()
    # else:
    #     form = UploadFileForm()
    data = {
        'title': 'О сайте',
        'posts': posts,
        'mainmenu': mainmenu,
        'page_obj': page_obj,
        # 'form': form,
    }
    # return render(request, 'places/about.html', context=data)
    return render(request, 'places/about.html', context=data)


def login(request):
    data = {
        'title': 'Авторизация',
        'posts': posts,
        'mainmenu': mainmenu,
    }
    return render(request, 'places/main.html', context=data)


class ShowPost(DataMixin, DetailView):
    model = Place
    template_name = 'places/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        person = People.objects.filter(place_id=context['post'].pk)
        return self.get_mixin_context(context, title = context['post'].title, person = person)


class AddPostPlace(View):

    def get(self, request):
        form = AddPostForm()
        data = {
            'mainmenu': mainmenu,
            'title': 'Добавление статьи',
            'form': form
        }
        return render(request, 'places/addpost.html', context=data)

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        data = {
            'mainmenu': mainmenu,
            'title': 'Добавление статьи',
            'form': form
        }
        return render(request, 'places/addpost.html', context=data)


class AddPostPerson(DataMixin, CreateView):
    form_class = AddPostFormPerson
    template_name = 'places/addpost.html'
    success_url = reverse_lazy('places')
    title_page = 'Добавление человека'


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

