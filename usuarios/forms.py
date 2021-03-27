from django import forms
from django.contrib.auth.models import User


class FormularioUsuarios(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese su contraseña',
        'id': 'password1',
        'required': 'required',
    }
    ))
    password2 = forms.CharField(label='Contraseña de confirmación', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese nuevamente su contraseña',
        'id': 'password2',
        'required': 'required',
    }
    ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico ', }),

            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese nombre de usuario ', }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese nombre ', }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su apellido ', })
        }
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('La contraseña no coincide')
        return password2