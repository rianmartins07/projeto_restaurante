from django import forms

from menu.models import Menu
from core.menu.choices import status


class MenuForm(forms.ModelForm):
    nome = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome...'
            }
        )
    )

    valor = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o valor...'
            }
        )
    )

    descricao = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a descrição...'
            }   
        )
    )

    status = forms.MultipleChoiceField(
        required=True,
        choices=status.choices,
        widget=forms.Select(
            attrs={
                'class' : 'form-control'
            }
        )
    )

    foto = forms.ImageField(
        required=True,
        widget=forms.FileInput(
            attrs={
                'class' : 'form-control-file'
            }
        )
    )
    
    class Meta:
        model = Menu
        fields = '__all__'
