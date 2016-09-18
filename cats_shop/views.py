from django.views.generic import ListView, DetailView
from .models import Album, Cat

class CatsList(ListView):
    queryset = Cat.objects.order_by('-date')
    context_object_name = 'cats_list'
    template_name = 'cats_shop/index.html'


class CatDetail(DetailView):
    model = Cat
    template_name = 'cats_shop/detail.html'
