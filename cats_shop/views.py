from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, FormView

from .models import Album, Cat, Order, OrderPosition
from .forms import OrderForm, RegistrationForm, LoginForm
from carton.cart import Cart

from django.contrib.auth import authenticate, login, logout


class CatsList(ListView):
    queryset = Cat.objects.filter(in_stock=True).order_by('-date')
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

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            initial_values = {'phone': request.user.profile.phone,
                              'name': request.user.get_full_name(),
                              'address': request.user.profile.address}
            order_form = OrderForm(initial=initial_values)
        else:
            order_form = OrderForm()
        return self.render_to_response(self.get_context_data(form=order_form))

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=%s' % (reverse('cats_shop:index'),
                                           ('Order adding canceled')))
        else:
            cart = Cart(request.session)

            if cart.items:
                order = Order()
                form = OrderForm(request.POST, instance=order)

                if form.is_valid():
                    order = form.save(commit=False)
                    if request.user.is_authenticated():
                        order.customer = request.user
                    else:
                        order.customer = None
                    form.save()
                else:
                    return self.form_invalid(form)

                for item in cart.items:
                    order_item = OrderPosition()
                    order_item.order = order
                    item.product.in_stock = False
                    item.product.save()
                    order_item.product = item.product
                    order_item.save()
                cart.clear()
                return super(OrderAddView, self).post(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(
                    u'%s?status_message=%s' % (reverse('cats_shop:index'),
                                               ('Your cart is empty')))


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
