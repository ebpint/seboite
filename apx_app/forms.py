from django import forms
from .models import CustomUser, ListaNegra, Operacion

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Usuario'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
    )
    perfil = forms.ChoiceField(
        choices=CustomUser.PERFIL_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

class BlacklistForm(forms.ModelForm):
    class Meta:
        model = ListaNegra
        fields = ['archivo']
        widgets = {
            'archivo': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.txt'
            })
        }

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operacion
        fields = ['archivo']
        widgets = {
            'archivo': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.txt'
            })
        }