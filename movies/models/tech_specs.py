"""Technical specification models."""

from django.db import models


class AspectRatio(models.Model):
    """Aspect ratio model."""

    aspect_ratio = models.DecimalField(max_digits=3, decimal_places=2, unique=True)

    class Meta:
        ordering = ["aspect_ratio"]
        verbose_name = "Aspect Ratio"

    def __str__(self):
        return f"{self.aspect_ratio}:1"


class GenreTag(models.Model):
    """Genre tags model."""

    genre = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["genre"]
        verbose_name = "Genre Tag"

    def __str__(self):
        return self.genre.title()


class RunTime(models.Model):
    """Movie run time model."""

    run_time = models.IntegerField(unique=True)

    class Meta:
        ordering = ["run_time"]
        verbose_name = "Run Time"

    def __str__(self):
        return f"{self.run_time} minutes"


class Year(models.Model):
    """Release year model."""

    year = models.IntegerField(unique=True, verbose_name="Release Year")

    class Meta:
        ordering = ["year"]

    def __str__(self):
        return str(self.year)
