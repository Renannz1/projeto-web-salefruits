# produto/forms.py

from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade', 'categoria'] 
    
    # Personalizando os campos do formulario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['preco'].label = 'Preço da Caixa'
        self.fields['quantidade'].label = 'Quantidade de Caixas'
        


# filtro para categorias
class FiltroProdutoForm(forms.Form):
    CATEGORIAS = (
        ('', 'Todas'),
        ('Fruta', 'Fruta'),
        ('Legume', 'Legume'),
        ('Verdura', 'Verdura'),
    )
    categoria = forms.ChoiceField(choices=CATEGORIAS, required=False, label='Categoria')