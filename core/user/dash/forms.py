from django import forms
from django.core.exceptions import ValidationError
from pycpfcnpj import cpfcnpj


from user.models import User
from user.choices import sexo


class UserForm(forms.ModelForm):
    nome = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    user = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    cpf = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    sexo = forms.MultipleChoiceField(
        required=True,
        choices=sexo.choices,
        widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
        )
    )

    dtnasc = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type' : 'date'
            }
        )
    )

    celular = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    

    def clean(self):
        self.cpf = ''.join(filter(str.isdigit, self.cpf))
        
    class Meta:
        model = User
        fields = '__all__'
