from django import forms
from apps.galeria.models import Fotografia

#ModelForm cria o formulário a partir do Model
class FotografiaForms(forms.ModelForm):

    class Meta:
        model = Fotografia
        exclude = ['publicada',] # campos que não irão aparecer
        labels = {
            'descricao':'Descrição',
            'data_fotografia': 'Data de Registro',
            'usuario': 'Usuário'
            
        }
        widgets = {
            'nome': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'legenda': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'categoria': forms.Select(
                attrs={'class':'form-control'}
            ),
            'descricao': forms.Textarea(
                attrs={'class':'form-control'}
            ),
            'foto': forms.FileInput(
                attrs={'class':'form-control'}
            ),
            'data_fotografia': forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'class':'form-control',
                    'type': 'date',
                },
            ),
            'usuario': forms.Select(
                attrs={'class':'form-control'},
            ),
            
        }
        