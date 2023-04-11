from django.db import models

class Sexo (models.TextChoices):
    MASCULINO = 'Masculino'
    FEMININO = 'Feminino'
    PREFIRO_NAO_DIZER = 'Prefiro não dizer'
    
class Role (models.TextChoices):
    GARCOM = 'Garçom'
    COZINHEIRO = 'Cozinheiro'
    ADMINISTRADOR = 'Administrador'
    OPERADOR_DE_CAIXA = 'Operador de Caixa'
    OUTRO = 'Outro'