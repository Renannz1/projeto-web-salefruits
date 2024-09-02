from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nome de usuário",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    confirm_password = forms.CharField(
        label="Confirmar Senha",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("As senhas não conferem.")
        
        return cleaned_data

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'cpf', 'telefone', 'endereco', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={"class": "form-control"}),
            'cpf': forms.TextInput(attrs={"class": "form-control"}),
            'telefone': forms.TextInput(attrs={"class": "form-control"}),
            'endereco': forms.TextInput(attrs={"class": "form-control"}),
            'descricao': forms.TextInput(attrs={"class": "form-control"}),
        }
