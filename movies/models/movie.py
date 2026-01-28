"""Movie model."""

from django.db import models


class Movie(models.Model):
    """Aggregate model for movies."""

    # Primary fields
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150, unique=True)
    director = models.ManyToManyField("Director", blank=True, through="DirectorPosition")

    # Crew fields
    composer = models.ManyToManyField("Composer", blank=True, through="ComposerPosition")
    dp = models.ManyToManyField("Cinematographer", verbose_name="Director of Photography", blank=True, through="CinematographerPosition")
    editor = models.ManyToManyField("Editor", blank=True, through="EditorPosition")
    prod_designer = models.ManyToManyField("ProdDesigner", verbose_name="Production Designer", blank=True, through="ProdDesignerPosition")
    writer = models.ManyToManyField("Writer", blank=True, through="WriterPosition")

    #Technical spec fields
    aspect_ratio = models.ForeignKey("AspectRatio", on_delete=models.PROTECT, null=True, blank=True)
    run_time = models.ForeignKey("RunTime", on_delete=models.PROTECT, null=True, blank=True)
    year = models.ForeignKey("Year", on_delete=models.PROTECT, null=True, blank=True)

    # Release info fields
    barcode = models.ForeignKey("Barcode", on_delete=models.PROTECT, null=True, blank=True)
    discs = models.ForeignKey("Discs", on_delete=models.PROTECT, null=True, blank=True)
    publisher = models.ForeignKey("Publisher", on_delete=models.PROTECT, null=True, blank=True)

    # MPAA info fields
    rating = models.ForeignKey("MPAARating", on_delete=models.PROTECT, null=True, blank=True)
    mpaa_cert = models.PositiveIntegerField(verbose_name="MPAA Certificate #", unique=True, null=True, blank=True)
    distributor = models.ForeignKey("Distributor", on_delete=models.PROTECT, null=True, blank=True)
    rating_reason = models.ManyToManyField("MPAARatingsReason", blank=True)

    # Genre tags
    genre = models.ManyToManyField("GenreTag", blank=True)

    class Meta:
        ordering = ["slug", "year"]

    def __str__(self):
        return self.title

    def get_directors(self):
        """Return list of editors in sequence order."""
        return self.directorposition_set.all().order_by("sequence")

    def get_composers(self):
        """Return list of editors in sequence order."""
        return self.composerposition_set.all().order_by("sequence")

    def get_dps(self):
        """Return list of editors in sequence order."""
        return self.cinematographerposition_set.all().order_by("sequence")

    def get_editors(self):
        """Return list of editors in sequence order."""
        return self.editorposition_set.all().order_by("sequence")

    def get_prod_designers(self):
        """Return list of editors in sequence order."""
        return self.proddesignerposition_set.all().order_by("sequence")

    def get_writers(self):
        """Return list of writers in sequence order."""
        return self.writerposition_set.all().order_by("sequence")
