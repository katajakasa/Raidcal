# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


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


class ProfilePasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ProfilePasswordChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                _('User password change'),
                'old_password',
                'new_password1',
                'new_password2',
                Submit('change_password', value=_('Change password'))
            )
        )


class ProfileUserChangeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileUserChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                _('User profile change'),
                'first_name',
                'last_name',
                'email',
                Submit('change_profile', value=_('Change profile'))
            )
        )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
