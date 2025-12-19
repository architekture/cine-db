from django.db import models


class AspectRatio(models.Model):
    """Aspect ratio model."""

    aspect_ratio = models.DecimalField(max_digits=3, decimal_places=2, unique=True)

    class Meta:
        ordering = ["aspect_ratio"]
        verbose_name = "Aspect Ratio"

    def __str__(self):
        return f"{self.aspect_ratio}:1"


class Barcode(models.Model):
    """Barcode model."""

    barcode = models.BigIntegerField(unique=True)

    class Meta:
        ordering = ["barcode"]

    def __str__(self):
        return str(self.barcode)


class Cinematographer(models.Model):
    """Cinematographer model."""

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, default="", blank=True)
    last_name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "middle_name", "last_name"],
                name="full_name_dp",
            ),
        ]
        ordering = ["last_name", "first_name", "middle_name"]

    def __str__(self):
        if self.middle_name != "":
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        elif self.middle_name == "" and self.last_name == "":
            return self.first_name
        else:
            return f"{self.first_name} {self.last_name}"


class Composer(models.Model):
    """Composer model."""

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, default="", blank=True)
    last_name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "middle_name", "last_name"],
                name="full_name_composer",
            ),
        ]
        ordering = ["last_name", "first_name", "middle_name"]

    def __str__(self):
        if self.middle_name != "":
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        elif self.middle_name == "" and self.last_name == "":
            return self.first_name
        else:
            return f"{self.first_name} {self.last_name}"


class Director(models.Model):
    """Director model."""

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, default="", blank=True)
    last_name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "middle_name", "last_name"],
                name="full_name_director",
            ),
        ]
        ordering = ["last_name", "first_name", "middle_name"]

    def __str__(self):
        if self.middle_name != "":
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        elif self.middle_name == "" and self.last_name == "":
            return self.first_name
        else:
            return f"{self.first_name} {self.last_name}"


class Discs(models.Model):
    """Number of discs model."""

    discs = models.IntegerField(unique=True)

    class Meta:
        ordering = ["discs"]
        verbose_name_plural = "discs"

    def __str__(self):
        return str(self.discs)


class Distributor(models.Model):
    """U.S. distributor model."""

    distributor = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["distributor"]

    def __str__(self):
        return self.distributor


class Editor(models.Model):
    """Editor model."""

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, default="", blank=True)
    last_name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "middle_name", "last_name"],
                name="full_name_editor",
            ),
        ]
        ordering = ["last_name", "first_name", "middle_name"]

    def __str__(self):
        if self.middle_name != "":
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        elif self.middle_name == "" and self.last_name == "":
            return self.first_name
        else:
            return f"{self.first_name} {self.last_name}"


class ProdDesigner(models.Model):
    """Production Designer model."""

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, default="", blank=True)
    last_name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "middle_name", "last_name"],
                name="full_name_prod_designer",
            ),
        ]
        ordering = ["last_name", "first_name", "middle_name"]
        verbose_name = "Production Designer"

    def __str__(self):
        if self.middle_name != "":
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        elif self.middle_name == "" and self.last_name == "":
            return self.first_name
        else:
            return f"{self.first_name} {self.last_name}"


class RunTime(models.Model):
    """Movie run time model."""

    run_time = models.IntegerField(unique=True)

    class Meta:
        ordering = ["run_time"]
        verbose_name = "Run Time"

    def __str__(self):
        return f"{self.run_time} minutes"


class Publisher(models.Model):
    """Disc publisher model."""

    publisher = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["publisher"]

    def __str__(self):
        return self.publisher


class Writer(models.Model):
    """Writer model."""

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, default="", blank=True)
    last_name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "middle_name", "last_name"],
                name="full_name_writer",
            ),
        ]
        ordering = ["last_name", "first_name", "middle_name"]

    def __str__(self):
        if self.middle_name != "":
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        elif self.middle_name == "" and self.last_name == "":
            return self.first_name
        else:
            return f"{self.first_name} {self.last_name}"


class Year(models.Model):
    """Release year model."""

    year = models.IntegerField(unique=True, verbose_name="Release Year")

    class Meta:
        ordering = ["year"]

    def __str__(self):
        return str(self.year)



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


class Movie(models.Model):
    """Aggregate model for movies."""

    # Primary fields
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150, unique=True)
    director = models.ManyToManyField(Director, blank=True)

    # Crew fields
    composer = models.ManyToManyField(Composer, blank=True)
    dp = models.ManyToManyField(Cinematographer, verbose_name="Director of Photography", blank=True)
    editor = models.ManyToManyField(Editor, blank=True)
    prod_designer = models.ManyToManyField(ProdDesigner, verbose_name="Production Designer", blank=True)
    writer = models.ManyToManyField(Writer, blank=True, through="WriterPosition")

    #Technical spec fields
    aspect_ratio = models.ForeignKey(AspectRatio, on_delete=models.PROTECT, null=True, blank=True)
    run_time = models.ForeignKey(RunTime, on_delete=models.PROTECT, null=True, blank=True)
    year = models.ForeignKey(Year, on_delete=models.PROTECT, null=True, blank=True)

    # Release info fields
    barcode = models.ForeignKey(Barcode, on_delete=models.PROTECT, null=True, blank=True)
    discs = models.ForeignKey(Discs, on_delete=models.PROTECT, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, null=True, blank=True)

    # MPAA info fields
    rating = models.ForeignKey(MPAARating, on_delete=models.PROTECT, null=True, blank=True)
    mpaa_cert = models.PositiveIntegerField(verbose_name="MPAA Certificate #", unique=True, null=True, blank=True)
    distributor = models.ForeignKey(Distributor, on_delete=models.PROTECT, null=True, blank=True)
    rating_reason = models.ManyToManyField(MPAARatingsReason, blank=True)

    class Meta:
        ordering = ["slug", "year"]

    def __str__(self):
        return self.title


class WriterPosition(models.Model):
    """Through model for adding sequence data to the junction table."""
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    crew_member = models.ForeignKey(Writer, on_delete=models.CASCADE)
    sequence = models.IntegerField()
