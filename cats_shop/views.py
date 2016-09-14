from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Album

class CatsList(ListView):
    model = Album
    context_object_name = 'cats_list'
    template_name = 'cats_shop/index.html'


class CatDetail(DetailView):
    model = Album
    context_object_name = 'cat'
    template_name = 'cats_shop/detail.html'
