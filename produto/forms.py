# produto/forms.py

from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade', 'categoria', 'imagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Produto'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição do Produto', 'rows': 3}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço da Caixa'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantidade de Caixas'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

    # Personalizando os campos do formulário
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['preco'].label = 'Preço da Caixa'
        self.fields['quantidade'].label = 'Quantidade de Caixas'
        self.fields['nome'].label = 'Nome do Produto'
        self.fields['descricao'].label = 'Descrição do Produto'
        self.fields['categoria'].label = 'Categoria'

        # Ajustando a aparência dos campos
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

# Filtro para categorias
class FiltroProdutoForm(forms.Form):
    CATEGORIAS = (
        ('', 'Todas'),
        ('Fruta', 'Fruta'),
        ('Legume', 'Legume'),
        ('Verdura', 'Verdura'),
    )
    categoria = forms.ChoiceField(
        choices=CATEGORIAS,
        required=False,
        label='Categoria',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
