from django import forms
from .models import Solicitacao

class SolicitarProdutoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = ['quantidade']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantidade'].label = 'Quantidade'
    
    def clean_quantidade(self):
        quantidade = self.cleaned_data['quantidade']
        if quantidade <= 0:
            raise forms.ValidationError('A quantidade deve ser maior que zero')
        return quantidade
