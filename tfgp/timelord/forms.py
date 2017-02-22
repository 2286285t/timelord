from django import forms
from timelord.models import UserAccount
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ('picture',)
