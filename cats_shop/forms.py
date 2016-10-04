from django.core.urlresolvers import reverse
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, ButtonHolder
from crispy_forms.bootstrap import FormActions

from .models import Order
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ['phone', 'name', 'address']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.form_action = reverse('cats_shop:order')

        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        self.helper.help_text_inline = True
        self.helper.html5_required = False
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-6'

        self.helper.layout = Layout(
            self.helper.layout, FormActions(
                Submit('add_button', 'Save', css_class="btn btn-primary"),
                Submit('cancel_button', 'Cancel', css_class="btn btn-link"),
            ))


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse('cats_shop:register')

        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.help_text_inline = True
        self.helper.html5_required = False

        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-6'

        self.helper.layout = Layout(
                'username',
                'password1',
                'password2',
                FormActions(
                    Submit('register', 'Create', css_class='btn-primary'),
                ))


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse('cats_shop:login')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.help_text_inline = True
        self.helper.html5_required = False
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-6'
        self.helper.layout = Layout(
            'username',
            'password',
            FormActions(
                Submit('login', 'Login', css_class='btn-primary')
            )
        )
