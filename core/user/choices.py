from django.db import models

class sexo (models.TextChoices):
    MASCULINO = 'Masculino'
    FEMININO = 'Feminino'
    PREFIRO_NAO_DIZER = 'Prefiro não dizer'