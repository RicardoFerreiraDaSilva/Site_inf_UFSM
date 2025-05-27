from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'data_publicacao']
        widgets = {
            'data_publicacao': forms.DateInput(attrs={'type': 'date'})
        }
