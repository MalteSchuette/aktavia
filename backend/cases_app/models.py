from django.conf import settings
from django.db import models

class Case(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "Aktiv"
        DORMANT = "dormant", "Ruhend"
        CLOSED = "closed", "Abgeschlossen"

    reference = models.CharField("Aktenzeichen", max_length=20, unique=True)
    client = models.CharField("Mandant", max_length=200)
    opponent = models.CharField("Gegner", max_length=200, blank=True)
    area_of_law = models.CharField("Rechtsgebiet", max_length=100)
    responsible_lawyer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="cases",
        verbose_name="Verantwortlicher Anwalt",
    )
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.ACTIVE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]
        verbose_name = "Mandat"
        verbose_name_plural = "Mandate"
    
    def __str__(self):
        return f"{self.reference} · {self.client} ./. {self.opponent}"