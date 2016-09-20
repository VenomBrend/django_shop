from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView

from .models import Album, Cat, Order, OrderPosition
from .forms import OrderForm
from carton.cart import Cart


class CatsList(ListView):
    queryset = Cat.objects.order_by('-date')
    context_object_name = 'cats_list'
    template_name = 'cats_shop/index.html'


class CatDetail(DetailView):
    model = Cat
    template_name = 'cats_shop/detail.html'


class OrderAddView(CreateView):
    model = Order
    template_name = 'cats_shop/order_add.html'
    form_class = OrderForm

    def get_success_url(self):
        return u'%s?status_message=%s' % (reverse('cats_shop:index'),
                                          ('Order added successfully!'))

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=%s' % (reverse('cats_shop:index'),
                                           ('Order adding canceled')))
        else:
            order = Order()
            form = OrderForm(request.POST, instance=order)
            order = form.save(commit=False)
            order.user = None
            if form.is_valid():
                order.save()
            cart = Cart(request.session)
            for item in cart.items:
                order_item = OrderPosition()
                order_item.order = order
                order_item.product = item.product
                order_item.save()
            cart.clear()
            return super(OrderAddView, self).post(request, *args, **kwargs)
