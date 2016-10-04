from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, FormView

from .forms import UserEditForm, ProfileEditForm

from django.contrib.auth.models import User
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


class UserProfileUpdate(FormView):
    template_name = 'profile_edit.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.id)
        user_edit_form = UserEditForm(instance=user)
        profile_edit_form = ProfileEditForm(instance=user.profile)
        context = super(UserProfileUpdate, self).get_context_data(
            user_edit_form=user_edit_form,
            profile_edit_form=profile_edit_form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        user = User.objects.get(pk=request.user.id)
        user_edit_form = UserEditForm(request.POST, instance=user)
        profile_edit_form = ProfileEditForm(request.POST)

        if user_edit_form.is_valid():
            created_user = user_edit_form.save(commit=False)
            profile_edit_form = ProfileEditForm(request.POST,
                                                instance=user.profile)
            if profile_edit_form.is_valid():
                created_user.save()
                profile_edit_form.save()
                return HttpResponseRedirect(
                    u'{}?status_message={}'.format(
                        reverse('profile', kwargs={'pk': request.user.id}),
                        ('User profile updated!')))
        else:
            return self.form_invalid(self, user_edit_form,
                                     profile_edit_form, **kwargs)

    def form_invalid(self, user_edit_form, profile_edit_form, **kwargs):
        return self.render_to_response(self.get_context_data(
            user_edit_form=user_edit_form,
            profile_edit_form=profile_edit_form))
