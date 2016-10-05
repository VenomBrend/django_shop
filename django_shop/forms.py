from django.core.urlresolvers import reverse
from django.forms import ModelForm

from crispy_forms.helper import FormHelper

from django.contrib.auth.models import User
from .models import UserProfile


class UserEditForm(ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.form_tag = False

        self.helper.help_text_inline = True
        self.helper.html5_required = False
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-6'


class ProfileEditForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ['phone', 'address']

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.form_tag = False

        self.helper.help_text_inline = True
        self.helper.html5_required = False
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-6'
