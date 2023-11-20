from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {
                'required': '',
                'name': 'username',
                'id': 'username',
                'type': 'text',
                'class': 'form-control bg-white border-left-0 border-md',
                'placeholder': 'Username',
                'maxlength': '100',
                'minlength': '4'
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'required': '',
                'name': 'email',
                'id': 'email',
                'type': 'email',
                'class': 'form-control bg-white border-left-0 border-md',
                'placeholder': 'Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'required': '',
                'name': 'password1',
                'id': 'password1',
                'type': 'password',
                'class': 'form-control bg-white border-left-0 border-md',
                'placeholder': 'Password',
                'maxlength': '100',
                'minlength': '4'
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'required': '',
                'name': 'password2',
                'id': 'password2',
                'type': 'password',
                'class': 'form-control bg-white border-left-0 border-md',
                'placeholder': 'Confirm Password',
                'maxlength': '100',
                'minlength': '4'
            }
        )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-white border-left-0 border-md',
            'id': 'login-username',
            'placeholder': 'Enter your Username',
            'required': '',
            'name': 'username',
            'type': 'username'
        }),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control bg-white border-left-0 border-md',
            'id': 'login-password',
            'placeholder': 'Enter your Password',
            'required': '',
            'name': 'password',
            'type': 'password',
        }),
    )

