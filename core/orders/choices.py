from django.db import models

class Status (models.TextChoices):
    PRONTO = 'PRONTO'
    EM_PREPARO = 'EM PREPARO'
    CANCELADO = 'CANCELADO'
    