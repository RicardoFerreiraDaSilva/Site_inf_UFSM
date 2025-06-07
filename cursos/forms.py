from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'data_publicacao']
        widgets = {
            'data_publicacao': forms.DateInput(attrs={'type': 'date'})
        }

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
