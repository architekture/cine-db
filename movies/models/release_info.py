"""Release-specific models."""

from django.db import models


class Barcode(models.Model):
    """Barcode model."""

    barcode = models.BigIntegerField(unique=True)

    class Meta:
        ordering = ["barcode"]

    def __str__(self):
        return str(self.barcode)


class Discs(models.Model):
    """Number of discs model."""

    discs = models.IntegerField(unique=True)

    class Meta:
        ordering = ["discs"]
        verbose_name_plural = "discs"

    def __str__(self):
        return str(self.discs)


class Publisher(models.Model):
    """Disc publisher model."""

    publisher = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["publisher"]

    def __str__(self):
        return self.publisher
