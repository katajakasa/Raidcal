# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.db import transaction

from django_summernote.widgets import SummernoteInplaceWidget
from raidcal.maincal.models import Topic, Message


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


class NewThreadForm(forms.Form):
    topic = forms.CharField(label=_('Topic'), max_length=32)
    content = forms.CharField(widget=SummernoteInplaceWidget(), required=True)

    def __init__(self, *args, **kwargs):
        super(NewThreadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.include_media = False
        self.helper.layout = Layout(
            Fieldset(
                _('Create a new thread'),
                'topic',
                'content',
                Submit('create', value=_('Create topic'))
            )
        )

    def save(self, user):
        with transaction.atomic():
            topic = Topic()
            topic.user = user
            topic.title = self.cleaned_data['topic']
            topic.save()
            message = Message()
            message.user = user
            message.content = self.cleaned_data['content']
            message.topic = topic
            message.save()
            return topic, message


class NewMessageForm(forms.Form):
    content = forms.CharField(widget=SummernoteInplaceWidget(), required=True)

    def __init__(self, *args, **kwargs):
        super(NewMessageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.include_media = False
        self.helper.layout = Layout(
            Fieldset(
                _('Send a new message'),
                'content',
                Submit('create', value=_('Send'))
            )
        )

    def save(self, topic, user):
        message = Message()
        message.user = user
        message.topic = topic
        message.content = self.cleaned_data['content']
        message.save()
        return message
