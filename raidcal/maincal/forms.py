# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.logged_user = None
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                _('Calendar login'),
                'username',
                'password',
                Submit('submit', _('Login'))
            )
        )


class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                _('New user registration'),
                'username',
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2',
                Submit('submit', _('Register'))
            )
        )

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
