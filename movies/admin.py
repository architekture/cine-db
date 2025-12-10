from django.contrib import admin

from movies.models import (
    AspectRatio,
    Barcode,
    Cinematographer,
    Composer,
    Director,
    Discs,
    Editor,
    Movie,
    ProdDesigner,
    Publisher,
    RunTime,
    Writer,
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
    )


models = [
    AspectRatio,
    Barcode,
    Cinematographer,
    Composer,
    Director,
    Discs,
    Editor,
    ProdDesigner,
    Publisher,
    RunTime,
    Writer,
    Year,
]

admin.site.register(Movie, MovieAdmin)
admin.site.register(models)
