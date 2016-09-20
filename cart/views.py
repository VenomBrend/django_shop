from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from carton.cart import Cart
from cats_shop.models import Cat


def add_to_cart(request, id):
    cart = Cart(request.session)
    cat = Cat.objects.get(id=id)
    if cat not in cart:
        cart.add(cat, price=cat.price)
        message = 'Cat was added to shopping cart'
    else:
        message = 'Cat already in the shopping cart'
    if 'cat' in request.path:
        return HttpResponseRedirect(reverse('cat'), message)
    else:
        return HttpResponseRedirect(
            '{}?status_message={}'.format(reverse('cats_shop:index'),
                                          message))


def remove_from_cart(request, id):
    cart = Cart(request.session)
    cat = Cat.objects.get(id=id)
    cart.remove(cat)
    message = 'Cat was removed from shopping cart'
    return HttpResponseRedirect(
            '{}?status_message={}'.format(reverse('cart:shopping-cart-show'),
                                          message))


def show_cart(request):
    return render(request, 'cart.html')


def clear_all(request):
    cart = Cart(request.session)
    cart.clear()
    return render(request, 'cart.html')
