from django import forms
from django.core.exceptions import ValidationError
from pycpfcnpj import cpfcnpj
from django.contrib.auth.models import Group


from user.models import User
from user.choices import Sexo


class UserForm(forms.ModelForm):

    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    last_name = forms.CharField(
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
        choices=Sexo.choices,
        widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
        )
    )
    
    data_nascimento = forms.DateField(
        required=True,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type' : 'date'
            }
        )
    )

    numero_celular = forms.CharField(
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
