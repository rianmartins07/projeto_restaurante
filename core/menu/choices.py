from django.db import models

class status (models.TextChoices):
    ATIVO = 'Ativo'
    INATIVO = 'Inativo'