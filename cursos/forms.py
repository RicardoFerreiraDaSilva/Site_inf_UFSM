from django import forms
from .models import Projeto

# forms.py (versão corrigida)
from django import forms
from .models import Projeto # Garanta que Projeto está importado

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        # ✅ Corrigido para 'data_criacao' e adicionados os novos campos opcionais
        fields = ['titulo', 'descricao', 'link', 'imagem']

from .models import Atividade

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['titulo', 'descricao', 'tipo', 'data', 'local', 'imagem']

from django import forms
from .models import Atividade

class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ['titulo', 'descricao', 'tipo', 'data', 'local', 'imagem']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }
        
from django import forms
from .models import ProjetoPET

class ProjetoPETForm(forms.ModelForm):
    class Meta:
        model = ProjetoPET
        fields = ['titulo', 'descricao', 'grupo', 'ordem']  
