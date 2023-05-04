from django import forms

from waiter.models import Table



class TableForm(forms.ModelForm):
    responsible_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Insira o nome do responsável...'
            }
        )
    )
    tale_number = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o Numero da mesa'
            }
        )
    )
    class Meta:
        fields = '__all__'
        model = Table