# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.conf import settings
from .models import ReservarHora, Project
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class CrearNuevaReservaForm(forms.ModelForm):
    class Meta:
        model = ReservarHora
        fields = ['title', 'description', 'project']

class CreateNewProyectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(CreateNewProyectForm, self).__init__(*args, **kwargs)

class CustomAuthenticationForm(AuthenticationForm):
    # Personaliza el formulario de inicio de sesión si es necesario
    pass

class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={'class': 'black-text'}),
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'black-text'}),
    )

    class Meta:
        model = User
        fields = ['username', 'password']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico')
    username = forms.CharField(label='Nombre de usuario')

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'username')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
