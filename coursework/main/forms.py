from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, CharField


class RegisterUserForm(UserCreationForm):
    username = CharField(label='', widget=TextInput(attrs={'class': 'input__field', 'placeholder': 'Логин'}))
    password1 = CharField(label='', widget=PasswordInput(attrs={'class': 'input__field', 'placeholder': 'Пароль'}))
    password2 = CharField(label='', widget=PasswordInput(attrs={'class': 'input__field', 'placeholder': 'Повтор пароля'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={'class': 'input__field', 'placeholder': 'Логин'}),
            'password1': PasswordInput(attrs={'class': 'input__field', 'placeholder': 'Придумайте пароль'}),
            'password2': PasswordInput(attrs={'class': 'input__field', 'placeholder': 'Повторите пароль'}),
        }
