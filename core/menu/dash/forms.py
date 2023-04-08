from django import forms

from menu.models import Menu


class MenuForm(forms.ModelForm):
    nome = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    valor = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    descricao = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }   
        )
    )

    status = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(
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
