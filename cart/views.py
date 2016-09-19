from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from carton.cart import Cart
from ..cats_shop.models import Cat


def add_to_cart(request):
    cart = Cart(request.session)
    cat = Cat.objects.get(id=request.GET.get('id'))
    cart.add(cat, price=cat.price)
    message = 'Cat was added to shopping cart'
    if 'cat' in request.path:
        return HttpResponseRedirect(reverse('cat'), message)
    else:
        return HttpResponseRedirect(reverse('index'), message)


def remove_from_cart(request):
    cart = Cart(request.session)
    cat = Cat.objects.get(id=request.GET.get('id'))
    cart.remove(cat)
    message = 'Cat was removed from shopping cart'
    render(request, 'cart/show-cart.html', {'message': message})


def show_cart(request):
    return render(request, 'cart/show-cart.html')