"""MPAA ratings models."""

from django.db import models


class Distributor(models.Model):
    """U.S. distributor model."""

    distributor = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["distributor"]

    def __str__(self):
        return self.distributor


class MPAARating(models.Model):
    """MPAA rating model."""

    rating = models.CharField(max_length=5, unique=True)

    class Meta:
        ordering = ["rating"]
        verbose_name="MPAA Rating"

    def __str__(self):
        return self.rating


class MPAARatingsReason(models.Model):
    """Reason given for assigned MPAA rating model."""

    reason = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["reason"]
        verbose_name = "MPAA Ratings Reason"
    
    def __str__(self):
        return self.reason
