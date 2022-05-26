from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
    field_order = ['username', 'email', 'password1', 'password2']
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'test-input',
                                                                            'placeholder': 'Логин'}))
    email = forms.EmailField(label="email", widget=forms.EmailInput(attrs={'class': 'email-input',
                                                                           'placeholder': 'Email'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                 'placeholder': 'Повторите Пароль'}))


class LoginUserForm(AuthenticationForm):
    email = forms.EmailField(label="email", widget=forms.EmailInput(attrs={'class': 'email-input',
                                                                           'placeholder': 'Email'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                 'placeholder': 'Пароль'}))

    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields.pop('username')

    def clean(self):
        user = User.objects.get(email=self.cleaned_data.get('email'))
        self.cleaned_data['username'] = user.username
        return super(LoginUserForm, self).clean()
