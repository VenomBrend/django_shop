from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, FormView

from .models import Album, Cat, Order, OrderPosition
from .forms import OrderForm, RegistrationForm, LoginForm
from carton.cart import Cart

from django.contrib.auth import authenticate, login, logout


class CatsList(ListView):
    queryset = Cat.objects.order_by('-date')
    context_object_name = 'cats_list'
    template_name = 'cats_shop/index.html'


class CatDetail(DetailView):
    model = Cat
    template_name = 'cats_shop/detail.html'


class OrderAddView(FormView):
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
                form.save()
            cart = Cart(request.session)
            for item in cart.items:
                order_item = OrderPosition()
                order_item.order = order
                order_item.product = item.product
                order_item.save()
            cart.clear()
            return super(OrderAddView, self).post(request, *args, **kwargs)


class LoginFormView(FormView):
    form_class = LoginForm
    template_name = "cats_shop/login.html"
    success_url = "/"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginFormView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(ListView):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('cats_shop:index'))


class RegisterFormView(FormView):
    form_class = RegistrationForm
    success_url = "/login/"
    template_name = "cats_shop/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)