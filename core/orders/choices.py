from django.db import models

class Status (models.TextChoices):
    PEDIDO_NA_COZINHA = "PEDIDO NA COZINHA"
    PRONTO = 'PRONTO'
    EM_PREPARO = 'EM PREPARO'
    CANCELADO = 'CANCELADO'

class FeedbackChoices (models.TextChoices):
    MUITO_RUIM = 'Muito ruim'
    RUIM = 'Ruim'
    REGULAR = 'Regular'
    BOM = 'Bom'
    MUITO_BOM = 'Muito bom'