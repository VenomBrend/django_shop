from django.views.generic import DetailView, UpdateView

from .models import UserProfile
from cats_shop.models import Order


class UserProfileDetail(DetailView):
    model = UserProfile
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileDetail, self).get_context_data(**kwargs)
        orders = Order.objects.all().filter(customer=kwargs['object'].user)
        context['orders'] = orders
        return context


class UserProfileUpdate(UpdateView):
    model = UserProfile
    fields = '__all__'
    template_name = 'profile_edit.html'
