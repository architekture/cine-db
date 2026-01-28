"""Crew member & position models."""

from django.db import models

class CrewMember(models.Model):
    """Base crew member model."""

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, default="", blank=True)
    last_name = models.CharField(max_length=100)

    class Meta:
        abstract = True
        constraints = [
            models.UniqueConstraint(
                fields=["first_name", "middle_name", "last_name"],
                name="full_name_%(class)s",
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


class Cinematographer(CrewMember):
    """Cinematographer model."""


class Composer(CrewMember):
    """Composer model."""


class Director(CrewMember):
    """Director model."""


class Editor(CrewMember):
    """Editor model."""


class ProdDesigner(CrewMember):
    """Production Designer model."""

    class Meta(CrewMember.Meta):
        verbose_name = "Production Designer"


class Writer(CrewMember):
    """Writer model."""


class CrewPosition(models.Model):
    """Base crew position model."""

    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    sequence = models.IntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ["movie", "sequence"]


class CinematographerPosition(CrewPosition):
    """Through model for adding sequence data to the junction table."""

    dp = models.ForeignKey(Cinematographer, on_delete=models.CASCADE)

    class Meta(CrewPosition.Meta):
        constraints = [
            models.UniqueConstraint(
                fields=["movie", "dp", "sequence"],
                name="movie_dp_seq"
            )
        ]

    def __str__(self):
        return str(self.dp)


class ComposerPosition(CrewPosition):
    """Through model for adding sequence data to the junction table."""

    composer = models.ForeignKey(Composer, on_delete=models.CASCADE)

    class Meta(CrewPosition.Meta):
        constraints = [
            models.UniqueConstraint(
                fields=["movie", "composer", "sequence"],
                name="movie_composer_seq"
            )
        ]

    def __str__(self):
        return str(self.composer)


class DirectorPosition(CrewPosition):
    """Through model for adding sequence data to the junction table."""

    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    class Meta(CrewPosition.Meta):
        constraints = [
            models.UniqueConstraint(
                fields=["movie", "director", "sequence"],
                name="movie_director_seq"
            )
        ]

    def __str__(self):
        return str(self.director)


class EditorPosition(CrewPosition):
    """Through model for adding sequence data to the junction table."""

    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)

    class Meta(CrewPosition.Meta):
        constraints = [
            models.UniqueConstraint(
                fields=["movie", "editor", "sequence"],
                name="movie_editor_seq"
            )
        ]

    def __str__(self):
        return str(self.editor)


class ProdDesignerPosition(CrewPosition):
    """Through model for adding sequence data to the junction table."""

    prod_designer = models.ForeignKey(ProdDesigner, on_delete=models.CASCADE)

    class Meta(CrewPosition.Meta):
        constraints = [
            models.UniqueConstraint(
                fields=["movie", "prod_designer", "sequence"],
                name="movie_prod_designer_seq"
            )
        ]

    def __str__(self):
        return str(self.prod_designer)


class WriterPosition(CrewPosition):
    """Through model for adding sequence data to the junction table."""

    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)

    class Meta(CrewPosition.Meta):
        constraints = [
            models.UniqueConstraint(
                fields=["movie", "writer", "sequence"],
                name="movie_writer_seq"
            )
        ]

    def __str__(self):
        return str(self.writer)
