from django.conf.urls import url
from cart.views import add_to_cart, remove_from_cart, show_cart, clear_all


urlpatterns = [
    url(r'^add/(?P<id>[0-9]+)$', add_to_cart, name='shopping-cart-add'),
    url(r'^remove/(?P<id>[0-9]+)$', remove_from_cart,
        name='shopping-cart-remove'),
    url(r'^show/$', show_cart, name='shopping-cart-show'),
    url(r'^clear/$', clear_all, name='shopping-cart-clear'),
    ]
