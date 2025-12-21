from django.contrib import admin

from movies.models import (
    AspectRatio,
    Barcode,
    Cinematographer,
    CinematographerPosition,
    Composer,
    ComposerPosition,
    Director,
    DirectorPosition,
    Discs,
    Distributor,
    Editor,
    EditorPosition,
    GenreTag,
    Movie,
    MPAARating,
    MPAARatingsReason,
    ProdDesigner,
    ProdDesignerPosition,
    Publisher,
    RunTime,
    Writer,
    WriterPosition,
    Year,
)


class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "slug",
        "title",
        "year",
        "aspect_ratio",
        "run_time",
        "publisher",
        "discs",
        "barcode",
        "distributor",
        "mpaa_cert",
    )


models = [
    AspectRatio,
    Barcode,
    Cinematographer,
    CinematographerPosition,
    Composer,
    ComposerPosition,
    Director,
    DirectorPosition,
    Discs,
    Distributor,
    Editor,
    EditorPosition,
    GenreTag,
    MPAARating,
    MPAARatingsReason,
    ProdDesigner,
    ProdDesignerPosition,
    Publisher,
    RunTime,
    Writer,
    WriterPosition,
    Year,
]

admin.site.register(Movie, MovieAdmin)
admin.site.register(models)
